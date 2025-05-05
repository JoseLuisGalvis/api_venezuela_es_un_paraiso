# main.py
# uvicorn main:app --reload --port 8002
from fastapi import FastAPI
from data import turistic_sites

app = FastAPI(title="API de Sitios Turísticos de Venezuela")

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de sitios turísticos de Venezuela"}

@app.get("/sitios")
def get_all_sites():
    return turistic_sites

@app.get("/sitios/{site_id}")
def get_site_by_id(site_id: int):
    sitio = next((s for s in turistic_sites if s["id"] == site_id), None)
    if sitio:
        return sitio
    return {"error": "Sitio no encontrado"}
