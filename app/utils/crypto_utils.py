"""
    Módulo con funciones para encriptar y desencriptar mensajes con AES-CBC.
"""
import os
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def load_key() -> bytes:
    """
    Carga la clave de encriptación desde el entorno y la devuelve como bytes.
    """
    key = os.getenv("ENCRYPTION_KEY")
    if not key:
        raise ValueError("La clave de encriptación no está definida en el entorno")

    key_bytes = bytes.fromhex(key)
    if len(key_bytes) != 16:  # AES de 128 bits (16 bytes)
        raise ValueError("La clave de encriptación debe ser de 16 bytes")

    return key_bytes

def encrypt_message(message: str) -> str:
    """
    Encripta un mensaje con AES-CBC y devuelve el mensaje encriptado en base64.
    """
    key = load_key()
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    # Concatenar IV y ciphertext separados por ':'
    return iv + ':' + ct

def decrypt_message(encrypted_message: str) -> str:
    """
    Desencripta un mensaje encriptado con AES-CBC y devuelve el texto plano.
    """
    key = load_key()
    try:
        iv_b64, ct_b64 = encrypted_message.split(':')  # Separamos el IV y el ciphertext
        iv = b64decode(iv_b64)
        ct = b64decode(ct_b64)

        # Asegurarse de que el IV tenga la longitud correcta (16 bytes)
        if len(iv) != 16:
            raise ValueError("El IV debe tener 16 bytes de longitud.")

        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)  # Desencriptamos y eliminamos el padding
        return pt.decode('utf-8')
    except ValueError as e:
        raise ValueError(f"Error al intentar desencriptar el mensaje: {str(e)}") from e
    except Exception as e:
        raise ValueError(f"Error desconocido en la desencriptación: {str(e)}") from e
