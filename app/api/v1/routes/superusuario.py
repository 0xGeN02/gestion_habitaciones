"""
Aqui se definen las rutas para el superusuario
"""

from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.superusuario import Superusuario, SuperusuarioCreate
from app.db.session import get_db

router = APIRouter()

