from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    """
    Modelo base de Usuario.
    """
    identificador: str
    nombre: str
    correo: EmailStr
    telefono: str

    class Config:
        from_attributes = True

class Usuario(UsuarioBase):
    """
    Modelo de Usuario.
    """
    id: int
    
class UsuarioCreate(UsuarioBase):
    """
    Modelo de creación de Usuario.
    """
    pass
