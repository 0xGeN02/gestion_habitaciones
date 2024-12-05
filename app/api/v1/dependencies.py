from fastapi import Depends
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession

async def get_database_session(db: AsyncSession = Depends(get_db)):
    return db
