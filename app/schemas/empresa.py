"""
Módulo de clases de esquemas de Empresa.
"""
from typing import List
from pydantic import BaseModel, EmailStr, ConfigDict
from app.utils.string_utils import SectorEnum, CIFPattern, PhoneNumber
from .empleado import Empleado
from .administrador import Administrador

class EmpresaBase(BaseModel):
    """
    Modelo base de Empresa.
    """
    sector: SectorEnum
    nombre: str
    cif: CIFPattern
    correo: EmailStr
    telefono: PhoneNumber
    password: str

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

class Empresa(EmpresaBase):
    """
    Modelo de Empresa.
    """
    id: int
    empleados: List[Empleado] = []
    administracion: List[Administrador] = []

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

class EmpresaCreate(EmpresaBase):
    """
    Modelo de creación de Empresa.
    """

class EmpresaUpdate(EmpresaBase):
    """
    Modelo de actualización de Empresa.
    """
