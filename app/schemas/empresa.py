from typing import List
from pydantic import BaseModel, EmailStr
from .usuario import Usuario
from .administrador import Administrador

class EmpresaBase(BaseModel):
    sector: str
    nombre: str
    identificador: str
    correo: EmailStr
    telefono: str

    class Config:
        """
        Configuraciones del modelo.
        """
        from_attributes = True

class Empresa(EmpresaBase):
    """
    Modelo de Empresa.
    """
    id: int
    usuarios: List[Usuario] = []
    administracion: List[Administrador] = []

    class Config:
        """
        Configuraciones del modelo.
        """
        from_attributes = True

class EmpresaCreate(EmpresaBase):
    """
    Modelo de creación de Empresa.
    """
    pass

class EmpresaUpdate(EmpresaBase):
    """
    Modelo de actualización de Empresa.
    """
    pass