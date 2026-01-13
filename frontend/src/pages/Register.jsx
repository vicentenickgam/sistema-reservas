import { useNavigate } from "react-router-dom";
import api from "../api/axios";

const Register = () => {
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = {
      email: e.target.email.value,
      username: e.target.username.value,
      password: e.target.password.value,
      rol: e.target.rol.value,
    };
    try {
      await api.post("auth/register/", data);
      alert("Usuario registrado correctamente");
      navigate("/login");
    } catch (err) {
      alert("Error al registrar: " + err.response?.data?.error || err.message);
    }
  };

  return (
    <div style={styles.container}>
      <h2>Registro</h2>
      <form onSubmit={handleSubmit} style={styles.form}>
        <input name="email" placeholder="Email" style={styles.input} />
        <input name="username" placeholder="Username" style={styles.input} />
        <input name="password" type="password" placeholder="Password" style={styles.input} />
        <select name="rol" style={styles.input}>
          <option value="CLIENTE">Cliente</option>
          <option value="PROPIETARIO">Propietario</option>
        </select>
        <button type="submit" style={styles.button}>Registrarse</button>
      </form>
      <p>
        ¿Ya tienes cuenta? <a href="/login">Inicia sesión</a>
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

export default Register;
