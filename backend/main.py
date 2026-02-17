from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="API de Demostración Didáctica",
    description="Backend moderno con FastAPI para la práctica de CI/CD",
    version="1.0.0"
)

# Configuración de CORS para permitir peticiones desde el Frontend (Vercel o local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, restringir a dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "El Backend está funcionando correctamente.",
        "docs": "/docs"
    }

@app.get("/api/data")
async def get_data():
    return {
        "items": [
            {"id": 1, "name": "Módulo CI/CD", "status": "Completado"},
            {"id": 2, "name": "Módulo Docker", "status": "En progreso"},
            {"id": 3, "name": "Módulo Despliegue", "status": "Pendiente"}
        ],
        "backend_engine": "FastAPI (Python)"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
