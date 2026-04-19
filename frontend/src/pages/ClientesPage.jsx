import { useEffect, useState } from "react";
import { getClientes } from "../api/resourcesService";

function ClientesPage() {
  const [data, setData] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    async function load() {
      try {
        const response = await getClientes();
        setData(Array.isArray(response) ? response : response.results || []);
      } catch (requestError) {
        setError(requestError.message);
      }
    }

    load();
  }, []);

  return (
    <section>
      <h2>Clientes</h2>
      {error && <p>{error}</p>}
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </section>
  );
}

export default ClientesPage;
