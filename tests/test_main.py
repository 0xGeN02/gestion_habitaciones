"""
This is the main test file for the project.
"""
import asyncio

def test_hello_world():
    """
    Test para verificar que el test funciona
    """
    assert True

async def test_async_example():
    """
    Test asincrónico de ejemplo
    """
    await asyncio.sleep(1)
    assert True
