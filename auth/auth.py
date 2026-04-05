from .models import UserRegister, UserLogin
from ..db import supabase
from fastapi import HTTPException, status

__all__ = [
    "register_user",
    "login_user",
    "logout_user"
]

# authentication operations
async def register_user(user_data: UserRegister):
    """
    [[Register User]]
    Registers a new user account with Supabase Auth services.
    Handles internal validation and triggers confirmation emails if enabled.
    """
    try:
        # Supabase sign_up handles account creation and credential basic validation
        response = supabase.auth.sign_up({
            "email": user_data.email,
            "password": user_data.password
        })
        
        # return user details upon successful creation
        return {
            "message": "User registered successfully!",
            "user": response.user
        }
    except Exception as e:
        # signup failed (eg. user already exists, invalid domain, etc.)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Registration failed: {str(e)}"
        )

async def login_user(user_data: UserLogin):
    """
    [[Login User]]
    Authenticates an existing user and returns a session token.
    The response includes 'access_token' and 'refresh_token'.
    """
    try:
        # verify credentials with Supabase Auth
        response = supabase.auth.sign_in_with_password({
            "email": user_data.email,
            "password": user_data.password
        })
        
        # session details include JWTs used for subsequent authorizations
        return {
            "message": "Login successful!",
            "session": response.session
        }
    except Exception as e:
        # login failed (eg. incorrect credentials)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Login failed: {str(e)}"
        )

async def logout_user():
    """
    [[Logout User]]
    Ends the user's current session with Supabase.
    Access tokens should be cleared from the client-side as well.
    """
    try:
        # Supabase sign_out clears session server-side
        supabase.auth.sign_out()
        return {"message": "You have been logged out successfully."}
    except Exception as e:
        # sign-out encountered an unexpected error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Logout failed: {str(e)}"
        )
