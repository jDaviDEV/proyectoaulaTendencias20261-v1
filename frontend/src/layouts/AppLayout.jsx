import { NavLink, Outlet } from "react-router-dom";
import { useAuth } from "../context/useAuth.js";

function AppLayout() {
  const { logout } = useAuth();

  return (
    <div className="app-shell">
      <header>
        <h1>Panel de Ventas</h1>
        <button type="button" onClick={logout}>
          Cerrar sesion
        </button>
      </header>

      <nav>
        <NavLink to="/">Dashboard</NavLink>
        <NavLink to="/clientes">Clientes</NavLink>
        <NavLink to="/productos">Productos</NavLink>
        <NavLink to="/cotizaciones">Cotizaciones</NavLink>
        <NavLink to="/facturas">Facturas</NavLink>
        <NavLink to="/pagos">Pagos</NavLink>
      </nav>

      <main>
        <Outlet />
      </main>
    </div>
  );
}

export default AppLayout;
