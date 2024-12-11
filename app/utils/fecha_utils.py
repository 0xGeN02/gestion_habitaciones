"""
    Utilidades para manejar fechas y horas
"""

from pydantic import constr

# Definir el regex de las horas de 00:00 a 23:59
HORA_REGEX_PATTERN = r'([01]\d|2[0-3]):([0-5]\d)'

# Definir el regex de conjunto de horas
HORARIO_REGEX_PATTERN = r'^' + HORA_REGEX_PATTERN + '-' + HORA_REGEX_PATTERN + '$'

# Definir los tipos personalizados utilizando las expresiones regulares
HoraRegex = constr(pattern=HORA_REGEX_PATTERN)
HorarioRegex = constr(pattern=HORARIO_REGEX_PATTERN)
