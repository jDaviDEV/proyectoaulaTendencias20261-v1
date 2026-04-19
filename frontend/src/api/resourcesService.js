import api from "./client";

export async function getClientes() {
  const { data } = await api.get("/cliente/");
  return data;
}

export async function getProductos() {
  const { data } = await api.get("/producto/");
  return data;
}

export async function getCotizaciones() {
  const { data } = await api.get("/cotizacion/");
  return data;
}

export async function getFacturas() {
  const { data } = await api.get("/factura/");
  return data;
}

export async function getPagos() {
  const { data } = await api.get("/pago/");
  return data;
}
