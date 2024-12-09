"""
    Aqui se definen las rutas de la API para el recurso Usuario
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.schemas.usuario import Usuario, UsuarioCreate
from app.services.usuario_service import get_usuarios, create_usuario as service_create_usuario
from app.db.session import get_db

router = APIRouter()

@router.get("/usuarios", response_model=List[Usuario])
async def route_read_usuarios(db: AsyncSession = Depends(get_db)):
    """
    Obtiene todos los usuarios de la base de datos.
    """
    usuarios = await get_usuarios(db)
    return usuarios

@router.post("/usuarios", response_model=Usuario)
async def route_create_usuario(usuario: UsuarioCreate, db: AsyncSession = Depends(get_db)):
    """
    Crea un nuevo usuario en la base de datos.
    """
    try:
        nuevo_usuario = await service_create_usuario(usuario, db)
        return nuevo_usuario
    except IntegrityError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Identificador o correo ya existe")

@router.get("/usuarios/{usuario_id}", response_model=Usuario)
async def route_read_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    """
    Obtiene un usuario por su ID.
    """
    usuario = await get_usuario_by_id(usuario_id, db)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/usuarios/{usuario_id}", response_model=Usuario)
async def route_update_usuario(usuario_id: int, usuario: UsuarioCreate, db: AsyncSession = Depends(get_db)):
    """
    Actualiza un usuario existente.
    """
    usuario_actualizado = await update_usuario(usuario_id, usuario, db)
    if not usuario_actualizado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_actualizado

@router.delete("/usuarios/{usuario_id}", response_model=Usuario)
async def route_delete_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    """
    Elimina un usuario por su ID.
    """
    usuario_eliminado = await delete_usuario(usuario_id, db)
    if not usuario_eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_eliminado