"""
Módulo que contiene la configuración de la base de datos.
"""
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Define la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

# Crea el motor asíncrono
engine = create_async_engine(DATABASE_URL, echo=True)

# Crea la fábrica de sesiones asíncronas
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependencia para obtener la sesión de la base de datos
async def get_db():
    """
    Dependencia para obtener la sesión de la base de datos
    """
    async with async_session() as session:
        yield session
