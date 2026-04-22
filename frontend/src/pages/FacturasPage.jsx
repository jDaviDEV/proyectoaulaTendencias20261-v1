import ResourceCrudPage from "../components/ResourceCrudPage.jsx";
import { facturaApi } from "../api/crudService.js";
import { downloadFacturaPdf } from "../utils/invoicePdf.js";

function FacturasPage() {
  return (
    <ResourceCrudPage
      service={facturaApi}
      title="Facturas"
      subtitle="Genera y consulta facturas a partir de cotizaciones. Lleva el control de pagos, estados y saldos pendientes de tus clientes."
      emptyTableMessage="No hay facturas registradas."
      hideCreateButton={false}
      createFields={["cotizacion_id"]}
      editFields={["fecha_anulacion", "fecha_vencimiento", "motivo_anulacion"]}
      onCreate={async (payload) => {
        const id = Number(payload?.cotizacion_id);
        if (!id || Number.isNaN(id)) {
          throw new Error("Ingrese un ID de cotización válido.");
        }
        await facturaApi.convertirDesdeCotizacion(id);
      }}
      onUpdate={async (id, payload) => {
        const body = {
          fecha_anulacion: payload?.fecha_anulacion ?? null,
          fecha_vencimiento: payload?.fecha_vencimiento ?? null,
          motivo_anulacion: payload?.motivo_anulacion ?? null,
        };
        await facturaApi.update(id, body);
      }}
      extraRowActions={(row) => (
        <button
          type="button"
          className="btn--link"
          onClick={async () => {
            try {
              await downloadFacturaPdf(row);
            } catch (err) {
              // Fallback simple para que el usuario no quede “sin respuesta”.
              // eslint-disable-next-line no-alert
              alert(err?.message || "No se pudo generar el PDF.");
              // eslint-disable-next-line no-console
              console.error(err);
            }
          }}
        >
          PDF
        </button>
      )}
    />
  );
}

export default FacturasPage;
