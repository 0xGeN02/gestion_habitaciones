"""
    Modulo con utilidades para la validación de strings
"""

from enum import Enum
from typing_extensions import Annotated
from pydantic import StringConstraints

class SectorEnum(str, Enum):
    """
    Enumeración de sectores de empresa
    """
    PRIMARIO = "primario"
    SECUNDARIO = "secundario"
    TERCIARIO = "terciario"

    @classmethod
    def values(cls):
        """
        Devuelve una lista con los valores de los sectores
        """
        return [sector.value for sector in cls]

# CIF Empresa 8 digitos Alfanumericos
CIF_REGEX_PATTERN = r'^[A-Z0-9]{8}$'
CIFPattern = Annotated[str, StringConstraints(pattern=CIF_REGEX_PATTERN)]

# DNI 8 digitos numericos y una letra
DNI_REGEX_PATTERN = r'^[0-9]{8}[A-Z]$'
DNIPattern = Annotated[str, StringConstraints(pattern=DNI_REGEX_PATTERN)]

# Patrón de expresión regular para un número de teléfono con o sin prefijo
PHONE_REGEX_PATTERN = r'^(\+[0-9]{2})?[0-9]{9}$'
PhoneNumber = Annotated[str, StringConstraints(pattern=PHONE_REGEX_PATTERN)]
