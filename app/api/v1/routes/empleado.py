"""
Define las rutas de la API para el recurso empleado
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.empleado import Empleado, EmpleadoCreate
from app.services.empleado_service import get_empleados, create_empleado
from app.db.session import get_db

router = APIRouter()

@router.get("/empleados", response_model=List[Empleado])
async def read_empleados(db: AsyncSession = Depends(get_db)):
    empleados = await get_empleados(db)
    return empleados

@router.post("/empleados", response_model=Empleado)
async def create_empleado(empleado: EmpleadoCreate, db: AsyncSession = Depends(get_db)):
    nuevo_empleado = await create_empleado(empleado, db)
    return nuevo_empleado
