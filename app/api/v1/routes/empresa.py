"""
Define las rutas de la API para la entidad Empresa
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.empresa import Empresa, EmpresaCreate
from app.services.empresa_service import get_empresas, create_empresa
from app.db.session import get_db

router = APIRouter()

@router.get("/empresas", response_model=List[Empresa])
async def read_empresas(db: AsyncSession = Depends(get_db)):
    empresas = await get_empresas(db)
    return empresas

@router.post("/empresas", response_model=Empresa)
async def create_empresa(empresa: EmpresaCreate, db: AsyncSession = Depends(get_db)):
    nueva_empresa = await create_empresa(empresa, db)
    return nueva_empresa
