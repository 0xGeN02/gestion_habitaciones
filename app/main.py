"""
Archivo principal de la aplicación, donde se definen las rutas de la API.
"""

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.routes import usuario, superusuario, sala, empresa, empleado, administrador
from app.api.v1.auth import auth_router, auth_user_router
from app.db.database import engine, Base

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager para crear la base de datos al iniciar la aplicación.
    """
    logger.info("Starting application...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    logger.info("Shutting down application...")

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(auth_user_router, prefix="/api/v1/auth/user", tags=["auth/usuarios"])
app.include_router(usuario.router, prefix="/api/v1", tags=["usuarios"])
app.include_router(superusuario.router, prefix="/api/v1", tags=["superusuarios"])
app.include_router(sala.router, prefix="/api/v1", tags=["salas"])
app.include_router(empresa.router, prefix="/api/v1", tags=["empresas"])
app.include_router(empleado.router, prefix="/api/v1", tags=["empleados"])
app.include_router(administrador.router, prefix="/api/v1", tags=["administradores"])
