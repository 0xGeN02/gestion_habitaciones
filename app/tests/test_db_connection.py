"""
Este script se encarga de testear la conexión a la base de datos.
"""
import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
from dotenv import load_dotenv

# Cargar las variables de entorno desde .env
load_dotenv()

# Leer la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está configurada en el archivo .env")

# Crear el motor de la base de datos
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async def test_connection():
    """
    Funcion que testea la conexion con la database
    """
    try:
        # Probar la conexión
        async with engine.connect() as connection:
            result = await connection.execute(text("SELECT 1"))
            scalar_result = result.scalar()
            print("Conexión exitosa a la base de datos:", scalar_result == 1)
    except OperationalError as e:
        print(f"Error al conectar a la base de datos: {e}")

if __name__ == "__main__":
    asyncio.run(test_connection())
