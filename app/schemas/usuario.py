"""
    Modulo de esquemas de Usuario.
"""
from pydantic import BaseModel, EmailStr, ConfigDict
from app.utils.string_utils import PhoneNumber, DNIPattern
from app.utils.crypto_utils import decrypt_message
class UsuarioBase(BaseModel):
    """
    Modelo base de Usuario.
    """
    nombre: str
    correo: EmailStr
    telefono: PhoneNumber
    dni: str

    model_config = ConfigDict(from_attributes=True)

class Usuario(UsuarioBase):
    """
    Modelo de Usuario.
    """
    id: int

    @property
    def dni(self):
        return decrypt_message(self.dni)

    @dni.setter
    def dni(self, value):
        self.dni = value
    
class UsuarioCreate(UsuarioBase):
    """
    Modelo de creación de Usuario.
    """
    dni: DNIPattern

class UsuarioUpdate(BaseModel):
    """
    Modelo para la actualización de un Usuario.
    """
    correo: EmailStr = None
    telefono: PhoneNumber = None
