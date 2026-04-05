from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ..db import supabase

# Security scheme to handle Bearer Token (JWT)
security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Dependency to verify the user token with Supabase and return the user details.
    Uses the provided Bearer token (JWT) from the Authorization header.
    """
    token = credentials.credentials
    try:
        # Check if the token is valid by getting the user.
        # Supabase will throw an error if the token is invalid or expired.
        response = supabase.auth.get_user(token)
        user = response.user
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
            )
        
        # User is authenticated successfully.
        return user
    except Exception as e:
        # If any error occurs, return 401 Unauthorized.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Could not validate credentials: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Alias for 'protected_path' to be used in routes.
protected_path = get_current_user
