import { createContext, useEffect, useState } from "react";
import api from "../api/axios";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [access, setAccess] = useState(null);
  const [loading, setLoading] = useState(true);

  const login = async (email, password) => {
    const res = await api.post("token/", { email, password });
    setAccess(res.data.access);
    localStorage.setItem("refresh", res.data.refresh);
    await loadUser(res.data.access);
  };

  const loadUser = async (token) => {
    try {
      const res = await api.get("auth/me/", {
        headers: { Authorization: `Bearer ${token}` },
      });
      setUser(res.data);
    } catch {
      logout();
    }
  };

  const logout = () => {
    setUser(null);
    setAccess(null);
    localStorage.removeItem("refresh");
  };

  // 👇 PERSISTENCIA
  useEffect(() => {
    const refresh = localStorage.getItem("refresh");

    const restoreSession = async () => {
      if (!refresh) {
        setLoading(false);
        return;
      }

      try {
        const res = await api.post("token/refresh/", { refresh });
        setAccess(res.data.access);
        await loadUser(res.data.access);
      } catch {
        logout();
      } finally {
        setLoading(false);
      }
    };

    restoreSession();
  }, []);

  return (
    <AuthContext.Provider
      value={{ user, access, login, logout, loading }}
    >
      {children}
    </AuthContext.Provider>
  );
};
