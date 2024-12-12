"""
Este módulo contiene funciones para eliminar y crear tablas en la base de datos.
"""

import asyncio
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.db.database import engine, Base

async def drop_tables():
    """Drop all tables in the database"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    print("Tables dropped successfully")

async def create_tables():
    """Create all tables in the database"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully")

async def main():
    """Main async function"""
    await drop_tables()
    await create_tables()

if __name__ == "__main__":
    asyncio.run(main())