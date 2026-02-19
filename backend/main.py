import os
import logging
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter

from .auth import router as auth_router
from .db import init_db

logger = logging.getLogger("uvicorn.error")

app = FastAPI(
    title="API de Demostración Didáctica",
    description="Backend moderno con FastAPI para la práctica de CI/CD",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Metrics
REQUEST_COUNT = Counter("app_requests_total", "Total HTTP requests")


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    REQUEST_COUNT.inc()
    response = await call_next(request)
    return response


@app.get("/metrics")
def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/")
async def root():
    return {"status": "online", "message": "Backend funcionando", "docs": "/docs"}


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


app.include_router(auth_router)


@app.on_event("startup")
def on_startup():
    try:
        init_db()
        logger.info("Database initialized")
    except Exception as e:
        logger.exception("Error initializing database: %s", e)
    # Sentry (optional)
    import sentry_sdk
    sentry_dsn = os.getenv("SENTRY_DSN")
    if sentry_dsn:
        sentry_sdk.init(dsn=sentry_dsn)


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
