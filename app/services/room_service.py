from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Room
from app.schemas.room import RoomCreate

async def get_rooms(db: AsyncSession):
    result = await db.execute(select(Room))
    return result.scalars().all()

async def create_room(room: RoomCreate, db: AsyncSession):
    new_room = Room(**room.dict())
    db.add(new_room)
    await db.commit()
    await db.refresh(new_room)
    return new_room
