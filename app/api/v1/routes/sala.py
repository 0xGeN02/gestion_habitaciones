"""
    Rutas de la API para el recurso Sala
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.schemas.sala import Sala, SalaCreate, SalaUpdate
from app.services.sala_service import get_salas, create_sala as service_create_sala, get_sala_by_id, update_sala, delete_sala
from app.db.session import get_db

router = APIRouter()

@router.get("/salas", response_model=List[Sala])
async def read_salas(db: AsyncSession = Depends(get_db)):
    salas = await get_salas(db)
    return salas

@router.post("/salas", response_model=Sala)
async def create_new_sala(sala: SalaCreate, db: AsyncSession = Depends(get_db)):
    try:
        nueva_sala = await service_create_sala(sala, db)
        return nueva_sala
    except IntegrityError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Identificador ya existe")

@router.get("/salas/{sala_id}", response_model=Sala)
async def read_sala(sala_id: int, db: AsyncSession = Depends(get_db)):
    sala = await get_sala_by_id(sala_id, db)
    if not sala:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    return sala

@router.put("/salas/{sala_id}", response_model=Sala)
async def update_existing_sala(sala_id: int, sala: SalaUpdate, db: AsyncSession = Depends(get_db)):
    sala_actualizada = await update_sala(sala_id, sala, db)
    if not sala_actualizada:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    return sala_actualizada

@router.delete("/salas/{sala_id}", response_model=Sala)
async def delete_existing_sala(sala_id: int, db: AsyncSession = Depends(get_db)):
    sala_eliminada = await delete_sala(sala_id, db)
    if not sala_eliminada:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    return sala_eliminada