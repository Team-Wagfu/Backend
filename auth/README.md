# Supabase Authentication and Authorization

This directory contains the logic for user authentication and path protection using Supabase.

## Setup

1.  Create a `.env` file in the root directory with the following variables:
    *   `SUPABASE_URL`: Your Supabase project URL.
    *   `SUPABASE_KEY`: Your Supabase project API key (anon or service role).
2.  Install dependencies:
    *   `pip install supabase python-dotenv`

## Components

### `db.py` (Centralized)
Handles the initialization of the Supabase client and provides database-related utilities. This file is located in the root directory and should be used project-wide.

### `auth/auth.py`
Contains functions for registering and logging in users with Supabase.

## User Registration and Login

You can use the `register_user` and `login_user` functions within your routes:

```python
from ..auth import register_user, login_user

# To register a new user
@router.post("/register")
async def register(user_data: UserRegister):
    return await register_user(user_data)

# To log in an existing user
@router.post("/login")
async def login(user_data: UserLogin):
    return await login_user(user_data)
```

Both functions use pydantic models (`UserRegister` and `UserLogin`) to ensure correct input.

## Session Management

Supabase handles session management using JSON Web Tokens (JWT). When a user logs in, they receive an `access_token` and a `refresh_token`.

### Client-Side Responsibilities
1.  **Token Storage**: Securely store the `access_token` and `refresh_token`.
2.  **Authorization Header**: Include the `access_token` in the `Authorization: Bearer <token>` header for all requests to protected routes.
3.  **Token Refresh**: If the `access_token` expires, use the `refresh_token` to obtain a new one from Supabase. (Most Supabase client SDKs handle this automatically).

### Backend Responsibilities
1.  **Token Validation**: The `protected_path` dependency automatically validates the JWT with Supabase on every request.
2.  **Logout**: The `logout_user()` function clears the session on the Supabase server.

## How to use `protected_path`

To protect a route, add the `protected_path` dependency to your route function:

```python
from fastapi import Depends
from ..auth import protected_path

@router.get("/protected")
async def protected_route(user: dict = Depends(protected_path)):
    return {"message": "You are authorized!", "user": user}
```

This ensures that only authenticated users can access the route. If the user is not authenticated, Supabase will handle the error accordingly.
