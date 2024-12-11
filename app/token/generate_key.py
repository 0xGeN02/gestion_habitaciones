"""
    Module to generate a key for the encryption of the token
"""
from Crypto.Random import get_random_bytes
key = get_random_bytes(16)
print(key.hex())
