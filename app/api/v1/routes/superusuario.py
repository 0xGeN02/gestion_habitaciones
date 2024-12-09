"""
Aqui se definen las rutas para el superusuario
"""

from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.superusuario import Superusuario, SuperusuarioCreate
from app.services.superusuario_service import get_superusuarios, create_superusuario
from app.db.session import get_db

router = APIRouter()

@router.get("/superusuarios", response_model=List[Superusuario])
async def route_read_superusuarios(db: AsyncSession = Depends(get_db)):
    """
    Obtiene todos los superusuarios de la base de datos.
    """
    superusuarios = await get_superusuarios(db)
    return superusuarios

@router.post("/superusuarios", response_model=Superusuario)
async def route_create_superusuario(superusuario: SuperusuarioCreate, db: AsyncSession = Depends(get_db)):
    """
    Crea un nuevo superusuario en la base de datos.
    """
    nuevo_superusuario = await create_superusuario(superusuario, db)
    return nuevo_superusuario

@router.put("/superusuarios/{superusuario_id}", response_model=Superusuario)
async def route_update_superusuario(superusuario_id: int, superusuario: Superusuario, db: AsyncSession = Depends(get_db)):
    """
    Actualiza un superusuario en la base de datos.
    """
    pass

@router.delete("/superusuarios/{superusuario_id}")
async def route_delete_superusuario(superusuario_id: int, db: AsyncSession = Depends(get_db)):
    """
    Elimina un superusuario de la base de datos.
    """
    pass
