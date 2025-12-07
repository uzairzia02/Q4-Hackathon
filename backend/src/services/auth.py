import jwt
from datetime import datetime, timedelta
from typing import Optional

# Placeholder for JWT-based authentication service.
# In a real scenario, this would involve:
# 1. User registration and login endpoints.
# 2. Hashing passwords securely.
# 3. Generating and validating JWT tokens.
# 4. Integrating with a database for user management.

SECRET_KEY = "your-secret-key" # In production, this should be an environment variable
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except jwt.PyJWTError:
        raise credentials_exception

# This service would also include functions for:
# - Authenticating users against a database
# - Managing user sessions
# - Providing dependency for FastAPI to get current user
