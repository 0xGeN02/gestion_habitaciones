# Proyecto de Arquitectura de Software

Este proyecto es una aplicación de ejemplo que demuestra la creación de APIs utilizando FastAPI, encriptación de datos sensibles, integración con PostgreSQL, gestión de dependencias con Poetry, autenticación JWT, uso de middleware, scripts de testing, desarrollo dirigido por pruebas (TDD), expresiones regulares (regex) y manejo de métodos HTTP.

## Características Principales

### Creación de APIs

Utilizamos FastAPI para crear APIs robustas y eficientes. Las rutas de la API están organizadas en módulos para facilitar su mantenimiento y escalabilidad.

### Encriptación de Datos

Implementamos encriptación AES-CBC para proteger datos sensibles como DNI y CIF de usuarios y empresas. La clave de encriptación se gestiona a través de variables de entorno.

### PostgreSQL

La base de datos utilizada es PostgreSQL, gestionada a través de SQLAlchemy y AsyncSession para operaciones asíncronas.

### Poetry

Poetry se utiliza para la gestión de dependencias y el empaquetado del proyecto, asegurando un entorno de desarrollo limpio y reproducible.

### Autenticación JWT

La autenticación se maneja mediante tokens JWT, proporcionando un método seguro y escalable para la autenticación de usuarios.

### Middleware

Se implementan middlewares para manejar tareas comunes como el registro de solicitudes y la gestión de errores.

### Scripts de Testing

Se incluyen scripts de testing en PowerShell para automatizar pruebas de registro y autenticación de usuarios.

### Desarrollo Dirigido por Pruebas (TDD)

El proyecto sigue la metodología TDD, asegurando que las pruebas se escriban antes del código de implementación para mejorar la calidad del software.

### Expresiones Regulares (Regex)

Se utilizan expresiones regulares para validar formatos de datos como el DNI, asegurando que los datos ingresados cumplan con los requisitos esperados.

### Métodos HTTP

Se manejan todos los métodos HTTP comunes (GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD, TRACE) con ejemplos de uso tanto en `curl` como en `Invoke-WebRequest` de PowerShell.

## Estructura del Proyecto

```ps1
/app
    /api
        /v1
            /auth
                routes.py
                test_login.ps1
                test_register.ps1
                test_user.ps1
            /routes
                usuario.py
                superusuario.py
                sala.py
                empresa.py
                empleado.py
                administrador.py
    /db
        models.py
        session.py
    /schemas
        usuario.py
        token.py
    /services
        usuario_service.py
    /utils
        crypto_utils.py
    main.py
/README.md
/HTTPRequests.md
/ENCRYPT.md
/AUTH.md
```

## Instalación y Configuración

### Requisitos

- Python 3.8+
- PostgreSQL
- Poetry

### Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/tu_proyecto.git
    cd tu_proyecto
    ```

2. Instala las dependencias:

    ```bash
    poetry install
    ```

3. Configura las variables de entorno:

    ```bash
    cp .env.example .env
    # Edita el archivo .env con tus configuraciones
    ```

4. Inicia la aplicación:

    ```bash
    poetry run uvicorn app.main:app --reload
    ```

## Uso de las APIs

Consulta los archivos `HTTPRequests.md`, `ENCRYPT.md` y `AUTH.md` para obtener detalles sobre cómo utilizar las diferentes APIs, encriptación de datos y autenticación.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría realizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
