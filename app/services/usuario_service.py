"""
    Módulo de servicios de usuario
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Usuario
from app.schemas.usuario import UsuarioCreate

async def get_usuarios(db: AsyncSession):
    result = await db.execute(select(Usuario))
    return result.scalars().all()

async def create_usuario(usuario: UsuarioCreate, db: AsyncSession):
    nuevo_usuario = Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    await db.commit()
    await db.refresh(nuevo_usuario)
    return nuevo_usuario

async def get_usuario_by_id(usuario_id: int, db: AsyncSession):
    result = await db.execute(select(Usuario).filter(Usuario.id == usuario_id))
    return result.scalar_one_or_none()

async def update_usuario(usuario_id: int, usuario: UsuarioCreate, db: AsyncSession):
    usuario_db = await get_usuario_by_id(usuario_id, db)
    if not usuario_db:
        return None
    for key, value in usuario.dict().items():
        setattr(usuario_db, key, value)
    await db.commit()
    await db.refresh(usuario_db)
    return usuario_db

async def delete_usuario(usuario_id: int, db: AsyncSession):
    usuario_db = await get_usuario_by_id(usuario_id, db)
    if not usuario_db:
        return None
    await db.delete(usuario_db)
    await db.commit()
    return usuario_db