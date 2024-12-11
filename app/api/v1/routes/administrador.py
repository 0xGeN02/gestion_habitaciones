"""
Este archivo se encarga de manejar las rutas de la API que tienen que ver con el administrador
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.administrador import Administrador, AdministradorCreate
from app.db.session import get_db

router = APIRouter()
