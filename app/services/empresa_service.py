"""
    Módulo de servicios de empresa
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Empresa
from app.schemas.empresa import EmpresaCreate

async def get_empresas(db: AsyncSession):
    """
    Obtiene todas las empresas de la base de datos.
    """
    result = await db.execute(select(Empresa))
    return result.scalars().all()

async def create_empresa(empresa: EmpresaCreate, db: AsyncSession):
    """
    Crea una nueva empresa en la base de datos.
    """
    nueva_empresa = Empresa(**empresa.model_dump())
    db.add(nueva_empresa)
    await db.commit()
    await db.refresh(nueva_empresa)
    return nueva_empresa

async def get_empresa_by_id(empresa_id: int, db: AsyncSession):
    """
    Obtiene una empresa por su ID.
    """
    result = await db.execute(select(Empresa).filter(Empresa.id == empresa_id))
    return result.scalar_one_or_none()

async def update_empresa(empresa_id: int, empresa: EmpresaCreate, db: AsyncSession):
    """
    Actualiza una empresa en la base de datos.
    """
    empresa_db = await get_empresa_by_id(empresa_id, db)
    if not empresa_db:
        return None
    for key, value in empresa.model_dump().items():
        setattr(empresa_db, key, value)
    await db.commit()
    await db.refresh(empresa_db)
    return empresa_db

async def delete_empresa(empresa_id: int, db: AsyncSession):
    """
    Elimina una empresa de la base de datos.
    """
    empresa_db = await get_empresa_by_id(empresa_id, db)
    if not empresa_db:
        return None
    await db.delete(empresa_db)
    await db.commit()
    return empresa_db
