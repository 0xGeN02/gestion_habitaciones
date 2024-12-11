"""
Este módulo contiene pruebas unitarias para el módulo crypto_utils.py.
"""
import pytest
from app.utils.crypto_utils import encrypt_message, decrypt_message

def test_encrypt_decrypt_message():
    """
    Test para encriptar y desencriptar un mensaje.
    """
    original_message = "TestMessage123"

    # Encriptar el mensaje
    encrypted_message = encrypt_message(original_message)
    assert encrypted_message != original_message  # Asegurarse de que el mensaje encriptado es diferente al original

    # Desencriptar el mensaje
    decrypted_message = decrypt_message(encrypted_message)
    assert decrypted_message == original_message  # Asegurarse de que el mensaje desencriptado es igual al original

def test_encrypt_message_is_different_each_time():
    """
    Test para asegurarse de que cada vez que se encripta un mensaje, el resultado
    """
    original_message = "TestMessage123"

    # Encriptar el mismo mensaje dos veces
    encrypted_message1 = encrypt_message(original_message)
    encrypted_message2 = encrypt_message(original_message)

    # Asegurarse de que los mensajes encriptados son diferentes
    assert encrypted_message1 != encrypted_message2

def test_decrypt_message_with_wrong_key(monkeypatch):
    """
    Test para desencriptar un mensaje con una clave incorrecta.
    """
    original_message = "TestMessage123"

    # Encriptar el mensaje
    encrypted_message = encrypt_message(original_message)

    # Cambiar la clave de desencriptación
    def mock_load_key():
        return b"wrongkeywrongkeywrongkeywrongkey"

    monkeypatch.setattr("app.utils.crypto_utils.load_key", mock_load_key)

    # Intentar desencriptar el mensaje con la clave incorrecta
    with pytest.raises(Exception):
        decrypt_message(encrypted_message)
