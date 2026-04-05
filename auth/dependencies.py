from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ..db import supabase
from .models import User

__all__ = [
    "protected_path"
]

# define security scheme for bearer token parsing
security = HTTPBearer()

# route protection dependencies
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    [[Get Current User]]
    [Description]
    Validates the bearer token (JWT) provided in request headers with Supabase.
    If the token is valid, returns the corresponding User object.
    Otherwise, raises a 401 Unauthorized exception.
    """
    token = credentials.credentials
    try:
        # fetch user details directly from Supabase via token verification
        response = supabase.auth.get_user(token)
        user = response.user
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User retrieval failed: No user found in Supabase response."
            )
        
        # return user context upon successful authentication
        return user
    except Exception as e:
        # token is invalid, expired, or something else went wrong
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Could not validate credentials: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"}
        )

# alias for 'protected_path' used across project routes
protected_path = get_current_user
