"""
This module contains the SQLAlchemy models for the entities of the application.
"""

from sqlalchemy import Column, Integer, String, Boolean, ARRAY, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.utils.crypto_utils import encrypt_message, decrypt_message

class Sala(Base):
    """
    SQLAlchemy model for the Sala entity.
    """
    __tablename__ = "salas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    capacidad = Column(Integer, nullable=False)
    reserva = Column(Boolean, default=False)
    horarios = Column(ARRAY(String), nullable=False)
    identificador = Column(String, unique=True, nullable=False)

class Empresa(Base):
    """
    SQLAlchemy model for the Empresa entity.
    """
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sector = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    telefono = Column(String, unique=True, nullable=False)
    cif = Column(String, nullable=False)
    password = Column(String, nullable=False)
    empleados = relationship("Empleado", back_populates="empresa", overlaps="administracion")
    administracion = relationship("Administrador", back_populates="empresa", overlaps="empleados")

    def __init__(self, **kwargs):
        """
        Constructor for the Empresa class
        """
        super().__init__(**kwargs)
        self.empleados = []
        self.administracion = []
        if 'cif' in kwargs:
            self.cif = encrypt_message(kwargs['cif'])

    def get_cif(self):
        """
        Decrypts and returns the CIF of the company.
        """
        return decrypt_message(self.cif)

class Usuario(Base):
    """
    SQLAlchemy model for the Usuario entity.
    """
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    telefono = Column(String, unique=True, nullable=False)
    dni = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, **kwargs):
        """
        Constructor for the Usuario class
        """
        super().__init__(**kwargs)
        if 'dni' in kwargs:
            self.dni = encrypt_message(kwargs['dni'])

    def get_dni(self):
        """
        Decrypts and returns the DNI of the user.
        """
        return decrypt_message(self.dni)

class Empleado(Usuario):
    """
    SQLAlchemy model for the Empleado entity.
    """
    __tablename__ = "empleados"

    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    empresa_id = Column(Integer, ForeignKey('empresas.id'))
    empresa = relationship("Empresa", back_populates="empleados")

class Administrador(Empleado):
    """
    SQLAlchemy model for the Administrador entity.
    """
    __tablename__ = "administradores"

    id = Column(Integer, ForeignKey('empleados.id'), primary_key=True)



class Superusuario(Administrador):
    """
    SQLAlchemy model for the Superusuario entity.
    """
    __tablename__ = "superusuarios"

    id = Column(Integer, ForeignKey('administradores.id'), primary_key=True)
