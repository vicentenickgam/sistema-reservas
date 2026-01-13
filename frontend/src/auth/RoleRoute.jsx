import { useContext } from "react";
import { Navigate } from "react-router-dom";
import { AuthContext } from "./AuthContext";

const RoleRoute = ({ children, role }) => {
  const { user } = useContext(AuthContext);

  // Mientras carga el usuario (opcional)
  if (!user) {
    return <Navigate to="/login" replace />;
  }

  // Verifica rol
  if (!user.roles.includes(role)) {
    return <Navigate to="/login" replace />;
  }

  return children;
};

export default RoleRoute;
