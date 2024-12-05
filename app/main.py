from fastapi import FastAPI
from app.api.v1.routes import rooms, bookings, users

app = FastAPI(title="Gestor de Salas de Reunión")

# Registrar los routers
app.include_router(rooms.router, prefix="/api/v1/rooms", tags=["Rooms"])
app.include_router(bookings.router, prefix="/api/v1/bookings", tags=["Bookings"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
