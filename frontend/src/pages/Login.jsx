import { useContext, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../auth/AuthContext";

const Login = () => {
  const { login, user } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const email = e.target.email.value;
    const password = e.target.password.value;
    await login(email, password);
  };

  // Redirigir según rol
  useEffect(() => {
    if (!user) return;
    if (user.roles.includes("CLIENTE")) navigate("/cliente");
    else if (user.roles.includes("PROPIETARIO")) navigate("/propietario");
  }, [user, navigate]);

  return (
    <div style={styles.container}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit} style={styles.form}>
        <input name="email" placeholder="Email" style={styles.input} />
        <input name="password" type="password" placeholder="Password" style={styles.input} />
        <button type="submit" style={styles.button}>Ingresar</button>
      </form>
      <p>
        ¿No tienes cuenta? <a href="/register">Regístrate</a>
      </p>
    </div>
  );
};

const styles = {
  container: { maxWidth: "400px", margin: "50px auto", textAlign: "center" },
  form: { display: "flex", flexDirection: "column", gap: "10px" },
  input: { padding: "10px", fontSize: "16px" },
  button: { padding: "10px", fontSize: "16px", cursor: "pointer" },
};

export default Login;
