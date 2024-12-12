"""
    Módulo de rutas de usuario autenticado.
"""
import logging
import re
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError, jwt

from app.db.session import get_db
from app.schemas.usuario import Usuario
from app.services.usuario_service import get_usuario_by_correo
from app.token.jwt import SECRET_KEY, ALGORITHM
from app.api.v1.auth.routes import oauth2_scheme
from app.utils.crypto_utils import decrypt_message

logger = logging.getLogger(__name__)

router = APIRouter()

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: AsyncSession = Depends(get_db)
) -> Usuario:
    """Get current authenticated user"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception from None

    user = await get_usuario_by_correo(email, db)
    if user is None:
        raise credentials_exception
    return user

@router.get("/me", response_model=Usuario)
async def read_users_me(
    current_user: Annotated[Usuario, Depends(get_current_user)],
    desencriptar: bool = False
):
    """
    Get current authenticated user with optional decryption
    """
    if desencriptar:
        try:
            if current_user.dni:
                # First decryption
                first_decryption = decrypt_message(current_user.dni)
                logger.debug("DNI after first decryption: %s", first_decryption)

                # Check if result is still encrypted
                if ':' in first_decryption:
                    # Second decryption
                    final_dni = decrypt_message(first_decryption)
                    logger.debug("DNI after second decryption: %s", final_dni)
                    current_user.dni = final_dni
                else:
                    current_user.dni = first_decryption

                # Validate DNI format
                if not re.match(r'^\d{8}[A-Z]$', current_user.dni):
                    logger.warning("Final DNI does not match expected format: %s", current_user.dni)

            if current_user.password:
                current_user.password = decrypt_message(current_user.password)
                logger.debug("Password decrypted successfully")

        except Exception as e:
            logger.error("Error decrypting user data: %s", str(e))
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error decrypting user data"
            ) from e

    return current_user
