// App.js
import { Routes, Route, Navigate } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import ClienteDashboard from "./pages/ClienteDashboard";
import PropietarioDashboard from "./pages/PropietarioDashboard";

import RoleRoute from "./auth/RoleRoute";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route
        path="/cliente"
        element={
          <RoleRoute role="CLIENTE">
            <ClienteDashboard />
          </RoleRoute>
        }
      />
      <Route
        path="/propietario"
        element={
          <RoleRoute role="PROPIETARIO">
            <PropietarioDashboard />
          </RoleRoute>
        }
      />
    </Routes>
  );
}

export default App;
