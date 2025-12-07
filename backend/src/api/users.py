from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from backend.src.services.auth import verify_access_token # Assuming auth service is in this path

router = APIRouter()

class UserProfile(BaseModel):
    hardware_tier: str
    experience_level: str
    learning_goals: List[str]

class User(BaseModel):
    id: str
    profile: UserProfile

# Placeholder for a user database
# In a real scenario, this would interact with Neon Postgres
fake_users_db = {}

@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user_id: str, profile: UserProfile):
    if user_id in fake_users_db:
        raise HTTPException(status_code=400, detail="User already registered")
    fake_users_db[user_id] = User(id=user_id, profile=profile)
    return fake_users_db[user_id]

@router.get("/users/{user_id}/profile", response_model=UserProfile)
def get_user_profile(user_id: str, current_user: str = Depends(verify_access_token)):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    # In a real app, current_user would be compared to user_id for authorization
    return fake_users_db[user_id].profile

@router.put("/users/{user_id}/profile", response_model=UserProfile)
def update_user_profile(user_id: str, profile: UserProfile, current_user: str = Depends(verify_access_token)):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    # In a real app, current_user would be compared to user_id for authorization
    fake_users_db[user_id].profile = profile
    return fake_users_db[user_id].profile

# Example of a login endpoint (simplified)
@router.post("/token")
async def login_for_access_token(username: str, password: str):
    # In a real scenario, hash password and verify against stored password
    if username == "testuser" and password == "testpass":
        access_token_expires = timedelta(minutes=30)
        access_token = create_access_token(
            data={"sub": username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
