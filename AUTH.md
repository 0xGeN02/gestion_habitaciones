# Autenticación en la API

Este documento describe las APIs de autenticación `login` y `register` y cómo usarlas desde la terminal.

## Registro de Usuario (`/register`)

La API de registro permite crear un nuevo usuario en el sistema y devuelve un token de acceso.

### Endpoint

```sh
POST /api/v1/auth/register
```

### Parámetros

- `nombre`: Nombre del usuario.
- `correo`: Correo electrónico del usuario.
- `telefono`: Teléfono del usuario.
- `dni`: DNI del usuario.
- `password`: Contraseña del usuario.

### Ejemplo de Solicitud

**Usando `curl`:**

```bash
curl -X POST http://example.com/api/v1/auth/register \
    -H "Content-Type: application/json" \
    -d '{
        "nombre": "Juan Perez",
        "correo": "juan.perez@example.com",
        "telefono": "123456789",
        "dni": "12345678A",
        "password": "password123"
    }'
```

**Usando `Invoke-WebRequest` en PowerShell:**

```powershell
Invoke-WebRequest -Uri http://example.com/api/v1/auth/register -Method POST -Body '{
    "nombre": "Juan Perez",
    "correo": "juan.perez@example.com",
    "telefono": "123456789",
    "dni": "12345678A",
    "password": "password123"
}' -ContentType "application/json"
```

### Respuesta

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}
```

## Inicio de Sesión (`/login`)

La API de inicio de sesión permite autenticar a un usuario y devuelve un token de acceso.

### Endpoint Login

```sh
POST /api/v1/auth/login
```

### Parámetros Login

- `username`: Correo electrónico del usuario.
- `password`: Contraseña del usuario.

### Ejemplo de Solicitud Login

**Usando `curl`:**

```bash
curl -X POST http://example.com/api/v1/auth/login \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d 'username=juan.perez@example.com&password=password123'
```

**Usando `Invoke-WebRequest` en PowerShell:**

```powershell
Invoke-WebRequest -Uri http://example.com/api/v1/auth/login -Method POST -Body @{
    username = "juan.perez@example.com"
    password = "password123"
} -ContentType "application/x-www-form-urlencoded"
```

### Respuesta Auth

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}
```

## Uso del Token de Acceso

El token de acceso devuelto por las APIs de registro e inicio de sesión debe ser utilizado en las solicitudes a otros endpoints protegidos de la API.

### Ejemplo de Solicitud con Token

**Usando `curl`:**

```bash
curl -X GET http://example.com/api/v1/protected/resource \
    -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Usando `Invoke-WebRequest` en PowerShell:**

```powershell
Invoke-WebRequest -Uri http://example.com/api/v1/protected/resource -Method GET -Headers @{
    Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

Este documento proporciona una guía rápida sobre cómo utilizar las APIs de autenticación `login` y `register` desde la terminal utilizando `curl` y `Invoke-WebRequest` en PowerShell.
