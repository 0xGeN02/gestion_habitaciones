"""
Administrador Service
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Administrador
from app.schemas.administrador import AdministradorCreate

async def get_administradores(db: AsyncSession):
    result = await db.execute(select(Administrador))
    return result.scalars().all()

async def create_administrador(administrador: AdministradorCreate, db: AsyncSession):
    nuevo_administrador = Administrador(**administrador.model_dump())
    db.add(nuevo_administrador)
    await db.commit()
    await db.refresh(nuevo_administrador)
    return nuevo_administrador