"""
Define las rutas de la API para el recurso empleado
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.empleado import Empleado, EmpleadoCreate
from app.db.session import get_db

router = APIRouter()
