"""
Este módulo contiene las funciones que interactúan con la base de datos para las salas.
"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Sala
from app.schemas.sala import SalaCreate, SalaUpdate

async def get_salas(db: AsyncSession):
    result = await db.execute(select(Sala))
    return result.scalars().all()

async def create_sala(sala: SalaCreate, db: AsyncSession):
    nueva_sala = Sala(**sala.dict())
    db.add(nueva_sala)
    await db.commit()
    await db.refresh(nueva_sala)
    return nueva_sala

async def get_sala_by_id(sala_id: int, db: AsyncSession):
    result = await db.execute(select(Sala).filter(Sala.id == sala_id))
    return result.scalar_one_or_none()

async def update_sala(sala_id: int, sala: SalaUpdate, db: AsyncSession):
    sala_db = await get_sala_by_id(sala_id, db)
    if not sala_db:
        return None
    for key, value in sala.dict().items():
        setattr(sala_db, key, value)
    await db.commit()
    await db.refresh(sala_db)
    return sala_db

async def delete_sala(sala_id: int, db: AsyncSession):
    sala_db = await get_sala_by_id(sala_id, db)
    if not sala_db:
        return None
    await db.delete(sala_db)
    await db.commit()
    return sala_db