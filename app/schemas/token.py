"""
Este archivo contiene los esquemas de los tokens.
"""
from pydantic import BaseModel

class Token(BaseModel):
    """
    Modelo de Token.
    """
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """
    Modelo de datos de Token.
    """
    correo: str | None = None
