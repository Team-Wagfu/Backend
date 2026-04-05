from pydantic import BaseModel, EmailStr
from ..db import supabase
from fastapi import HTTPException, status

# Models for request data
class UserRegister(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

async def register_user(user_data: UserRegister):
    """
    Registers a new user with Supabase Auth.
    """
    try:
        # Supabase sign_up handles internal validation
        response = supabase.auth.sign_up({
            "email": user_data.email,
            "password": user_data.password
        })
        
        # User is successfully created
        return {
            "message": "User registered successfully!",
            "user": response.user
        }
    except Exception as e:
        # If signup fails (e.g. user already exists)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Registration failed: {str(e)}"
        )

async def login_user(user_data: UserLogin):
    """
    Authenticates a user with Supabase Auth and returns the session.
    """
    try:
        # Supabase sign_in_with_password handles credential verification
        response = supabase.auth.sign_in_with_password({
            "email": user_data.email,
            "password": user_data.password
        })
        
        # Session includes access_token, which should be used for future requests.
        return {
            "message": "Login successful!",
            "session": response.session
        }
    except Exception as e:
        # If login fails (wrong credentials, etc.)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Login failed: {str(e)}"
        )
