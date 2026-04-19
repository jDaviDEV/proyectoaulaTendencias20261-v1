import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { healthCheck } from "../api/authService";
import { useAuth } from "../context/useAuth.js";

function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [healthStatus, setHealthStatus] = useState("");
  const [localError, setLocalError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const { login, authError } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const redirectTo = location.state?.from?.pathname || "/";

  async function handleHealthCheck() {
    setLocalError("");
    setHealthStatus("Verificando conexion...");
    try {
      const data = await healthCheck();
      setHealthStatus(data.message || "Conexion correcta");
    } catch (error) {
      setHealthStatus("");
      setLocalError(error.message);
    }
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setLocalError("");
    setIsLoading(true);

    const ok = await login(username, password);
    setIsLoading(false);

    if (ok) {
      navigate(redirectTo, { replace: true });
    }
  }

  return (
    <section>
      <h2>Iniciar sesion</h2>

      <button type="button" onClick={handleHealthCheck}>
        Probar conexion API
      </button>
      {healthStatus && <p>{healthStatus}</p>}

      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Usuario</label>
        <input
          id="username"
          type="text"
          value={username}
          onChange={(event) => setUsername(event.target.value)}
          required
        />

        <label htmlFor="password">Contrasena</label>
        <input
          id="password"
          type="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
          required
        />

        <button type="submit" disabled={isLoading}>
          {isLoading ? "Ingresando..." : "Entrar"}
        </button>
      </form>

      {(localError || authError) && <p>{localError || authError}</p>}
    </section>
  );
}

export default LoginPage;
