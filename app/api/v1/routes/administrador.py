"""
Este archivo se encarga de manejar las rutas de la API que tienen que ver con el administrador
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.administrador import Administrador, AdministradorCreate
from app.services.administrador_service import get_administradores, create_administrador
from app.db.session import get_db

router = APIRouter()

@router.get("/administradores", response_model=List[Administrador])
async def read_administradores(db: AsyncSession = Depends(get_db)):
    """
    Obtiene todos los administradores
    """
    administradores = await get_administradores(db)
    return administradores

@router.post("/administradores", response_model=Administrador)
async def create_administrador(administrador: AdministradorCreate, db: AsyncSession = Depends(get_db)):
    """
    Crea un nuevo administrador
    """
    nuevo_administrador = await create_administrador(administrador, db)
    return nuevo_administrador
