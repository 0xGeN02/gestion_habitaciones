from pydantic import BaseModel

class RoomCreate(BaseModel):
    name: str
    capacity: int
    location: str

class RoomUpdate(BaseModel):
    name: str | None = None
    capacity: int | None = None
    location: str | None = None

class RoomResponse(BaseModel):
    id: int
    name: str
    capacity: int
    location: str
