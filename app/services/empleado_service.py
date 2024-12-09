"""
Servicios de empleado
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Empleado
from app.schemas.empleado import EmpleadoCreate

async def get_empleados(db: AsyncSession):
    result = await db.execute(select(Empleado))
    return result.scalars().all()

async def create_empleado(empleado: EmpleadoCreate, db: AsyncSession):
    nuevo_empleado = Empleado(**empleado.dict())
    db.add(nuevo_empleado)
    await db.commit()
    await db.refresh(nuevo_empleado)
    return nuevo_empleado