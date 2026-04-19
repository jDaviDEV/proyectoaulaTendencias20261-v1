import { useEffect, useState } from "react";
import { getFacturas } from "../api/resourcesService";

function FacturasPage() {
  const [data, setData] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    async function load() {
      try {
        const response = await getFacturas();
        setData(Array.isArray(response) ? response : response.results || []);
      } catch (requestError) {
        setError(requestError.message);
      }
    }

    load();
  }, []);

  return (
    <section>
      <h2>Facturas</h2>
      {error && <p>{error}</p>}
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </section>
  );
}

export default FacturasPage;
