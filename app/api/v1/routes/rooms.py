from fastapi import APIRouter, HTTPException
from app.schemas.room import RoomCreate, RoomUpdate, RoomResponse

router = APIRouter()

# Mock de base de datos
rooms = {}

@router.get("/", response_model=list[RoomResponse])
async def list_rooms():
    return list(rooms.values())

@router.post("/", response_model=RoomResponse)
async def create_room(room: RoomCreate):
    new_id = len(rooms) + 1
    rooms[new_id] = {"id": new_id, **room.dict()}
    return rooms[new_id]

@router.put("/{room_id}", response_model=RoomResponse)
async def update_room(room_id: int, room: RoomUpdate):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")
    rooms[room_id].update(room.dict(exclude_unset=True))
    return rooms[room_id]

@router.delete("/{room_id}", response_model=dict)
async def delete_room(room_id: int):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")
    del rooms[room_id]
    return {"message": "Room deleted successfully"}
