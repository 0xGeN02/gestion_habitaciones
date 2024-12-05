from fastapi import APIRouter, HTTPException
from app.schemas.booking import BookingCreate, BookingResponse

router = APIRouter()

# Mock de base de datos para reservas
bookings = {}

@router.get("/", response_model=list[BookingResponse])
async def list_bookings():
    return list(bookings.values())

@router.post("/", response_model=BookingResponse)
async def create_booking(booking: BookingCreate):
    new_id = len(bookings) + 1
    bookings[new_id] = {"id": new_id, **booking.dict()}
    return bookings[new_id]

@router.delete("/{booking_id}", response_model=dict)
async def delete_booking(booking_id: int):
    if booking_id not in bookings:
        raise HTTPException(status_code=404, detail="Booking not found")
    del bookings[booking_id]
    return {"message": "Booking deleted successfully"}
