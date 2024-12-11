# HTTP Requests

Este documento describe las diferentes solicitudes HTTP utilizadas en nuestro proyecto, lo que hace cada una y cómo manejar casos especiales como TRACE desde la terminal debido al poco soporte en los navegadores.

## GET

La solicitud GET se utiliza para recuperar datos del servidor. Es una solicitud segura y no modifica el estado del recurso.

**Ejemplo:**

```bash
curl -X GET http://example.com/api/resource
```

**Ejemplo en PowerShell:**

```powershell
Invoke-WebRequest -Uri http://example.com/api/resource -Method GET
```

## POST

La solicitud POST se utiliza para enviar datos al servidor para crear un nuevo recurso. Esta solicitud puede modificar el estado del servidor.

**Ejemplo:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://example.com/api/resource
```

**Ejemplo en PowerShell:**

```powershell
Invoke-WebRequest -Uri http://example.com/api/resource -Method POST -Body '{"key":"value"}' -ContentType "application/json"
```

## PUT

La solicitud PUT se utiliza para actualizar un recurso existente en el servidor. Si el recurso no existe, puede crearlo.

**Ejemplo:**

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"key":"value"}' http://example.com/api/resource/1
```

**Ejemplo en PowerShell:**

```powershell
Invoke-WebRequest -Uri http://example.com/api/resource/1 -Method PUT -Body '{"key":"value"}' -ContentType "application/json"
```

## DELETE

La solicitud DELETE se utiliza para eliminar un recurso del servidor.

**Ejemplo:**

```bash
curl -X DELETE http://example.com/api/resource/1
```

**Ejemplo en PowerShell:**

```powershell
Invoke-WebRequest -Uri http://example.com/api/resource/1 -Method DELETE
```

## PATCH

La solicitud PATCH se utiliza para aplicar modificaciones parciales a un recurso.

**Ejemplo:**

```bash
curl -X PATCH -H "Content-Type: application/json" -d '{"key":"new_value"}' http://example.com/api/resource/1
```

**Ejemplo en PowerShell:**

```powershell
Invoke-WebRequest -Uri http://example.com/api/resource/1 -Method PATCH -Body '{"key":"new_value"}' -ContentType "application/json"
```

## OPTIONS

La solicitud OPTIONS se utiliza para describir las opciones de comunicación para el recurso de destino.

**Ejemplo:**

```bash
curl -X OPTIONS http://example.com/api/resource
```

**Ejemplo en PowerShell:**

```powershell
Invoke-WebRequest -Uri http://example.com/api/resource -Method OPTIONS
```

## HEAD

La solicitud HEAD es idéntica a GET, pero sin el cuerpo de la respuesta. Se utiliza para obtener los encabezados de la respuesta.

**Ejemplo:**

```bash
curl -I http://example.com/api/resource
```

**Ejemplo en PowerShell:**

```powershell
Invoke-WebRequest -Uri http://example.com/api/resource -Method HEAD
```

## TRACE

La solicitud TRACE se utiliza para realizar una prueba de bucle de retorno de mensaje a lo largo de la ruta al recurso de destino. Debido al poco soporte en los navegadores, se recomienda utilizar la terminal.

**Ejemplo:**

```bash
curl -X TRACE http://example.com/api/resource
```

**Ejemplo en PowerShell:**

```powershell
Invoke-WebRequest -Uri http://example.com/api/resource -Method TRACE
```

## Cómo trabajar con TRACE desde la terminal

Debido a que muchos navegadores no soportan la solicitud TRACE por razones de seguridad, es recomendable utilizar herramientas de línea de comandos como `curl` o `Invoke-WebRequest` para realizar estas solicitudes.

**Ejemplo:**

```bash
curl -X TRACE http://example.com/api/resource
```

**Ejemplo en PowerShell:**

```powershell
Invoke-WebRequest -Uri http://example.com/api/resource -Method TRACE
```

Recuerda siempre verificar las políticas de seguridad y permisos antes de utilizar la solicitud TRACE en un entorno de producción.
