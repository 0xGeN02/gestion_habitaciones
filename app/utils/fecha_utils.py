"""
    Utilidades para manejar fechas y horas
"""

from pydantic import constr

# Definir el regex de las horas de 00:00 a 23:59
HoraRegexPattern = r'([01]\d|2[0-3]):([0-5]\d)'

# Definir el regex de conjunto de horas
HorarioRegexPattern = r'^' + HoraRegexPattern + '-' + HoraRegexPattern + '$'

# Definir los tipos personalizados utilizando las expresiones regulares
HoraRegex = constr(pattern=HoraRegexPattern)
HorarioRegex = constr(pattern=HorarioRegexPattern)