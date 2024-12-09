"""
    Modulo responsable de la logica de negocio de la entidad Empresa
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Empresa
from app.schemas.empresa import EmpresaCreate

async def get_empresas(db: AsyncSession):
    """
    Obtiene todas las empresas
    """
    result = await db.execute(select(Empresa))
    return result.scalars().all()

async def create_empresa(empresa: EmpresaCreate, db: AsyncSession):
    """
    Crea una nueva empresa
    """
    nueva_empresa = Empresa(**empresa.model_dump())
    db.add(nueva_empresa)
    await db.commit()
    await db.refresh(nueva_empresa)
    return nueva_empresa
