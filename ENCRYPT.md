# Encriptación en la API

Este documento describe el método de encriptación utilizado en nuestra API para proteger los DNI y CIF de usuarios y empresas utilizando AES-CBC.

## Descripción del Método

Utilizamos el algoritmo de encriptación AES (Advanced Encryption Standard) en modo CBC (Cipher Block Chaining) para encriptar y desencriptar los DNI y CIF. Este método proporciona un alto nivel de seguridad al garantizar que los datos encriptados no puedan ser fácilmente descifrados sin la clave correcta.

### Clave de Encriptación

La clave de encriptación se carga desde una variable de entorno llamada `ENCRYPTION_KEY`. Esta clave debe ser de 16 bytes (128 bits) para ser compatible con AES-128.

### Encriptación

Para encriptar un mensaje (DNI o CIF), se realiza lo siguiente:

1. Se carga la clave de encriptación.
2. Se crea un nuevo objeto de cifrado AES en modo CBC.
3. Se encripta el mensaje utilizando la clave y se aplica padding para que el mensaje tenga un tamaño múltiplo del tamaño del bloque.
4. Se codifica el IV (vector de inicialización) y el ciphertext en base64 y se concatenan separados por `:`.

**Ejemplo de código:**

```python
def encrypt_message(message: str) -> str:
    key = load_key()
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    return iv + ':' + ct
```

### Desencriptación

Para desencriptar un mensaje encriptado, se realiza lo siguiente:

1. Se carga la clave de encriptación.
2. Se separan el IV y el ciphertext del mensaje encriptado.
3. Se decodifican el IV y el ciphertext de base64.
4. Se crea un nuevo objeto de cifrado AES en modo CBC utilizando el IV.
5. Se desencripta el ciphertext y se elimina el padding para obtener el mensaje original.

**Ejemplo de código:**

```python
def decrypt_message(encrypted_message: str) -> str:
    key = load_key()
    iv_b64, ct_b64 = encrypted_message.split(':')
    iv = b64decode(iv_b64)
    ct = b64decode(ct_b64)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')
```

## Uso en la API

En nuestra API, los DNI y CIF de usuarios y empresas se encriptan antes de almacenarse en la base de datos y se desencriptan cuando se necesitan para operaciones internas.

### Ejemplo de Encriptación de DNI

```python
dni = "12345678A"
encrypted_dni = encrypt_message(dni)
print(f"DNI encriptado: {encrypted_dni}")
```

### Ejemplo de Desencriptación de DNI

```python
encrypted_dni = "IV:Ciphertext"
decrypted_dni = decrypt_message(encrypted_dni)
print(f"DNI desencriptado: {decrypted_dni}")
```

## Consideraciones de Seguridad

- Asegúrate de que la clave de encriptación esté bien protegida y no se exponga en el código fuente.
- Cambia la clave de encriptación periódicamente para mejorar la seguridad.
- Verifica que el IV utilizado tenga siempre 16 bytes de longitud.

Este método garantiza que los datos sensibles como los DNI y CIF estén protegidos contra accesos no autorizados y se mantengan seguros en la base de datos.
