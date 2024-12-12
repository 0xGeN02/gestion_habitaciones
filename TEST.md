# Testing del Proyecto

Este documento describe cómo realizar los tests del proyecto utilizando Poetry y cómo ejecutar los tests de autenticación en PowerShell.

## Tests con Poetry

### Estructura de la Carpeta de Tests

La carpeta `/tests/` contiene todos los tests del proyecto organizados por módulos. Asegúrate de que todos los archivos de test sigan la convención de nombres `test_*.py`.

### Ejecución de Tests

Para ejecutar todos los tests del proyecto, utiliza el siguiente comando:

```bash
poetry run pytest
```

Este comando ejecutará todos los tests en la carpeta `/tests/` y generará un reporte con los resultados.

### Ejemplo de Test

A continuación se muestra un ejemplo de un archivo de test para el módulo de usuarios:

```python
# filepath: /tests/test_usuario.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_get_usuario_by_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/usuarios/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
```

## Tests de Autenticación en PowerShell

### Test de Registro

El script `test_register.ps1` realiza una prueba de registro de usuario y verifica que la respuesta sea exitosa.

**Ejemplo de Ejecución:**

```powershell
.\app\api\v1\auth\test_register.ps1
```

### Test de Inicio de Sesión

El script `test_login.ps1` realiza una prueba de inicio de sesión de usuario y verifica que la respuesta sea exitosa.

**Ejemplo de Ejecución:**

```powershell
.\app\api\v1\auth\test_login.ps1
```

### Test de Usuario Autenticado

El script `test_user.ps1` realiza una prueba para obtener la información del usuario autenticado utilizando el token de acceso.

**Ejemplo de Ejecución:**

```powershell
.\app\api\v1\auth\test_user.ps1
```

## Ejecución de Todos los Tests de Autenticación

Para ejecutar todos los tests de autenticación en PowerShell, puedes utilizar el siguiente comando:

```powershell
.\app\api\v1\auth\test_register.ps1; .\app\api\v1\auth\test_login.ps1; .\app\api\v1\auth\test_user.ps1
```

Este documento proporciona una guía rápida sobre cómo realizar los tests del proyecto utilizando Poetry y cómo ejecutar los tests de autenticación en PowerShell.
