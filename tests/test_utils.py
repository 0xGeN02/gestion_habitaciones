"""
Módulo de pruebas para las funciones de utilidad de la aplicación.
"""
import os
import sys
import re
from hypothesis import given, strategies as st
from hypothesis import settings

# Asegurarse de que el directorio raíz del proyecto esté en el PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.utils.string_utils import CIF_REGEX_PATTERN, DNI_REGEX_PATTERN, SectorEnum, PHONE_REGEX_PATTERN

@given(st.from_regex(CIF_REGEX_PATTERN))
@settings(max_examples=5)  # Limitar el número de ejemplos generados
def test_generate_cif(cif):
    """
    Test para verificar que se generan CIFs válidos
    """
    print(f"Generated CIF: {cif}")
    assert re.match(CIF_REGEX_PATTERN, cif)

@given(st.from_regex(DNI_REGEX_PATTERN))
@settings(max_examples=5)  # Limitar el número de ejemplos generados
def test_generate_dni(dni):
    """
    Test para verificar que se generan DNIs válidos
    """
    print(f"Generated DNI: {dni}")
    assert re.match(DNI_REGEX_PATTERN, dni)

@given(st.from_regex(PHONE_REGEX_PATTERN))
@settings(max_examples=5)  # Limitar el número de ejemplos generados
def test_generate_phone(phone):
    """
    Test para verificar que se generan números de teléfono válidos
    """
    print(f"Generated Phone: {phone}")
    assert re.match(PHONE_REGEX_PATTERN, phone)

@given(st.sampled_from(SectorEnum.values()))
@settings(max_examples=5)  # Limitar el número de ejemplos generados
def test_generate_sector(sector):
    """
    Test para verificar que se generan sectores válidos
    """
    print(f"Generated Sector: {sector}")
    assert sector in SectorEnum.values()

if __name__ == "__main__":
    test_generate_cif()
    test_generate_dni()
    test_generate_phone()
    test_generate_sector()
