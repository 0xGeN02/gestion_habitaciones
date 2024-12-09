from sqlalchemy import Column, Integer, String, Boolean, ARRAY, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

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
    identificador = Column(String, unique=True, nullable=False)
    correo = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    empleados = relationship("Empleado", back_populates="empresa", overlaps="administracion")
    administracion = relationship("Administrador", back_populates="empresa", overlaps="empleados")

class Usuario(Base):
    """
    SQLAlchemy model for the Usuario entity.
    """
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    identificador = Column(String, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
    correo = Column(String, nullable=False)
    telefono = Column(String, nullable=False)

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
