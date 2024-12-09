from app.schemas.usuario import Usuario

class Empleado(Usuario):
    """
    Modelo de Empleado.
    """
    empresa_id: int

class EmpleadoCreate(Empleado):
    """
    Modelo de creación de Empleado.
    """
    pass

class EmpleadoUpdate(Empleado):
    """
    Modelo de actualización de Empleado.
    """
    pass
