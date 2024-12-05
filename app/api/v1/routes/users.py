from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

# Mock de base de datos para usuarios
users = {}

@router.get("/", response_model=list[UserResponse])
async def list_users():
    return list(users.values())

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    new_id = len(users) + 1
    users[new_id] = {"id": new_id, **user.dict()}
    return users[new_id]

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted successfully"}
