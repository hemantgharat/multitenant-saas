from fastapi import FastAPI, Request, Response
from app.api.v1 import health
import uuid
import contextvars
from app.core.logging import request_id_context
import logging
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

app = FastAPI()

# ✅ Middleware setup
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    request_id_context.set(request_id)
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response

@app.on_event("startup")
async def startup_event():
    logging.info("Application startup")

@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Application shutdown")

app.include_router(health.router, prefix="/api/health", tags=["health-check"])
