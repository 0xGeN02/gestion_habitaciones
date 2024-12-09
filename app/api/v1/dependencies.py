"""
This file contains the dependencies that are used in the API endpoints.
"""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

async def get_database_session(db: AsyncSession = Depends(get_db)):
    """
    This function returns the database session.
    """
    return db
