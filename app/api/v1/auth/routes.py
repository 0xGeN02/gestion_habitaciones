"""
Routes for authentication
"""
import logging
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from app.db.session import get_db
from app.schemas.usuario import UsuarioCreate
from app.schemas.token import Token
from app.services.usuario_service import create_usuario, get_usuario_by_correo
from app.token.jwt import create_access_token
from app.utils.crypto_utils import decrypt_message

logger = logging.getLogger(__name__)

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

@router.post("/register", response_model=Token)
async def register(usuario: UsuarioCreate, db: AsyncSession = Depends(get_db)):
    """Register a new user and return access token"""
    try:
        nuevo_usuario = await create_usuario(usuario, db)
        access_token = create_access_token(data={"sub": nuevo_usuario.correo})
        return {"access_token": access_token, "token_type": "bearer"}
    except SQLAlchemyError as e:
        error_msg = str(e)
        if "usuarios_telefono_key" in error_msg:
            raise HTTPException(status_code=400, detail="El teléfono ya está registrado") from e
        elif "usuarios_correo_key" in error_msg:
            raise HTTPException(status_code=400, detail="El correo ya está registrado") from e
        elif "usuarios_dni_key" in error_msg:
            raise HTTPException(status_code=400, detail="El DNI ya está registrado") from e
        raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(e)}") from e
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    try:
        usuario = await get_usuario_by_correo(form_data.username, db)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Decrypt stored password
        stored_decrypted = decrypt_message(usuario.password)
        logger.debug("Login attempt - Password verification")
        logger.debug("Raw password provided: %s", form_data.password)
        logger.debug("Stored decrypted password: %s", stored_decrypted)

        # Direct comparison of raw passwords
        if form_data.password != stored_decrypted:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token = create_access_token(data={"sub": usuario.correo})
        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        logger.error("Login error: %s", str(e))
        if isinstance(e, HTTPException):
            raise
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        ) from e
