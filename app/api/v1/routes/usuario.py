"""
    Aqui se definen las rutas de la API para el recurso Usuario
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.schemas.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from app.services.usuario_service import create_usuario as service_create_usuario, get_usuario_by_id, delete_usuario_by_id, update_usuario as service_update_usuario
from app.db.session import get_db
from app.utils.crypto_utils import decrypt_message

router = APIRouter()

@router.post("/usuario", response_model=Usuario)
async def route_create_usuario(usuario: UsuarioCreate, db: AsyncSession = Depends(get_db)):
    """
    Crea un nuevo usuario
    """
    try:
        nuevo_usuario = await service_create_usuario(usuario, db)
        return nuevo_usuario
    except IntegrityError as exec:
        raise HTTPException(status_code=400, detail="El usuario ya existe.") from exec

@router.get("/usuario/{usuario_id}", response_model=Usuario)
async def route_read_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    """
    Obtiene un usuario por su id
    """
    usuario = await get_usuario_by_id(usuario_id, db)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Intenta desencriptar el DNI si está presente
    try:
        usuario.dni = decrypt_message(usuario.dni)
    except ValueError:
        raise HTTPException(status_code=500, detail="Error al desencriptar el DNI")

    return usuario

@router.delete("/usuario/{usuario_id}")
async def route_delete_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    """
    Elimina un usuario por su id
    """
    return await delete_usuario_by_id(usuario_id, db)

@router.put("/usuario/{usuario_id}", response_model=Usuario)
async def route_update_usuario(usuario_id: int, usuario_update: UsuarioUpdate, db: AsyncSession = Depends(get_db)):
    """
    Actualiza el correo o el teléfono de un usuario
    """
    return await service_update_usuario(usuario_id, usuario_update, db)
