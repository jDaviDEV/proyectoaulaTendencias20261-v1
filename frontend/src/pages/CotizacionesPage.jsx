import { useEffect, useState } from "react";
import { getCotizaciones } from "../api/resourcesService";

function CotizacionesPage() {
  const [data, setData] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    async function load() {
      try {
        const response = await getCotizaciones();
        setData(Array.isArray(response) ? response : response.results || []);
      } catch (requestError) {
        setError(requestError.message);
      }
    }

    load();
  }, []);

  return (
    <section>
      <h2>Cotizaciones</h2>
      {error && <p>{error}</p>}
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </section>
  );
}

export default CotizacionesPage;
