"""
Este módulo contiene funciones para eliminar y crear tablas en la base de datos.
"""

import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from app.db.models import Base
from app.db.session import DATABASE_URL

# Crear el motor de la base de datos
engine = create_async_engine(DATABASE_URL, echo=True)

async def drop_tables():
    """
    Elimina todas las tablas de la base de datos.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

async def create_tables():
    """
    Crea todas las tablas de la base de datos.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Función principal asíncrona
async def main():
    """
    Función principal asíncrona.
    """
    await drop_tables()
    await create_tables()

# Crear y ejecutar manualmente el bucle de eventos
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
