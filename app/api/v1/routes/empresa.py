"""
    Rutas de la API para el recurso Empresa
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.schemas.empresa import Empresa, EmpresaCreate
from app.services.empresa_service import get_empresas, create_empresa as service_create_empresa, get_empresa_by_id, update_empresa, delete_empresa
from app.db.session import get_db

router = APIRouter()

@router.get("/empresas", response_model=List[Empresa])
async def read_empresas(db: AsyncSession = Depends(get_db)):
    empresas = await get_empresas(db)
    return empresas

@router.post("/empresas", response_model=Empresa)
async def create_new_empresa(empresa: EmpresaCreate, db: AsyncSession = Depends(get_db)):
    try:
        nueva_empresa = await service_create_empresa(empresa, db)
        return nueva_empresa
    except IntegrityError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Identificador o correo ya existe")

@router.get("/empresas/{empresa_id}", response_model=Empresa)
async def read_empresa(empresa_id: int, db: AsyncSession = Depends(get_db)):
    empresa = await get_empresa_by_id(empresa_id, db)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return empresa

@router.put("/empresas/{empresa_id}", response_model=Empresa)
async def update_existing_empresa(empresa_id: int, empresa: EmpresaCreate, db: AsyncSession = Depends(get_db)):
    empresa_actualizada = await update_empresa(empresa_id, empresa, db)
    if not empresa_actualizada:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return empresa_actualizada

@router.delete("/empresas/{empresa_id}", response_model=Empresa)
async def delete_existing_empresa(empresa_id: int, db: AsyncSession = Depends(get_db)):
    empresa_eliminada = await delete_empresa(empresa_id, db)
    if not empresa_eliminada:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return empresa_eliminada