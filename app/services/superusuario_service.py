"""
Superusuario Service
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Superusuario
from app.schemas.superusuario import SuperusuarioCreate

async def get_superusuarios(db: AsyncSession):
    result = await db.execute(select(Superusuario))
    return result.scalars().all()

async def create_superusuario(superusuario: SuperusuarioCreate, db: AsyncSession):
    nuevo_superusuario = Superusuario(**superusuario.dict())
    db.add(nuevo_superusuario)
    await db.commit()
    await db.refresh(nuevo_superusuario)
    return nuevo_superusuario