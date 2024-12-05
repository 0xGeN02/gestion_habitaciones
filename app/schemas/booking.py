from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    room_id: int
    user_id: int
    start_time: datetime
    end_time: datetime

class BookingResponse(BaseModel):
    id: int
    room_id: int
    user_id: int
    start_time: datetime
    end_time: datetime
