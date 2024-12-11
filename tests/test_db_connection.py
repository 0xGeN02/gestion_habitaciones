import os
import asyncio
import pytest
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text
from dotenv import load_dotenv
# Crear el motor de la base de datos
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

@pytest.mark.asyncio
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