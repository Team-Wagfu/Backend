from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, List, Union, Dict, Optional, Any
from datetime import datetime

__all__ = [
    "UserRegister",
    "UserLogin",
    "User",
    "UserAppMetadata",
    "UserIdentity"
]

# request models
class UserRegister(BaseModel):

    '''
    [[User Register Model]]
    [Example]
    {
        "email": "user@example.com",
        "password": "securepassword123"
    }

    [Description]
    Data required to register a new user account via Supabase Auth.
    '''

    email: Annotated[
        EmailStr,
        Field(
            ...,
            description="Email address of the user",
            example="user@example.com"
        )
    ]
    password: Annotated[
        str,
        Field(
            ...,
            min_length=8,
            description="Password for the new account (min 8 characters)",
            example="securepassword123"
        )
    ]

class UserLogin(BaseModel):

    '''
    [[User Login Model]]
    [Example]
    {
        "email": "user@example.com",
        "password": "securepassword123"
    }

    [Description]
    Credentials required to authenticate an existing user.
    '''

    email: Annotated[
        EmailStr,
        Field(
            ...,
            description="Email address of the user",
            example="user@example.com"
        )
    ]
    password: Annotated[
        str,
        Field(
            ...,
            description="Password for the account",
            example="securepassword123"
        )
    ]

# internal / response models
class UserAppMetadata(BaseModel):

    '''
    [[User App Metadata]]
    [Description]
    Application-specific metadata returned by Supabase for a user.
    '''

    provider: Annotated[
        Optional[str],
        Field(
            None,
            description="The authentication provider used",
            example="email"
        )
    ]
    providers: Annotated[
        Optional[List[str]],
        Field(
            None,
            description="List of all providers linked to this user"
        )
    ]

class UserIdentity(BaseModel):

    '''
    [[User Identity]]
    [Description]
    Identity information linked to a Supabase user account.
    '''

    id: Annotated[
        str,
        Field(
            ...,
            description="Unique identity ID"
        )
    ]
    user_id: Annotated[
        str,
        Field(
            ...,
            description="ID of the user this identity belongs to"
        )
    ]
    identity_data: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            description="Additional data provided by the identity provider"
        )
    ]
    provider: Annotated[
        str,
        Field(
            ...,
            description="The name of the identity provider"
        )
    ]
    last_sign_in_at: Annotated[
        Optional[datetime],
        Field(
            None,
            description="Timestamp of the last sign in using this identity"
        )
    ]
    created_at: Annotated[
        Optional[datetime],
        Field(
            None,
            description="Timestamp when this identity was created"
        )
    ]
    updated_at: Annotated[
        Optional[datetime],
        Field(
            None,
            description="Timestamp when this identity was last updated"
        )
    ]

class User(BaseModel):

    '''
    [[User Model]]
    [Example]
    {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "email": "user@example.com",
        "role": "authenticated",
        "created_at": "2024-03-20T12:00:00Z"
    }

    [Description]
    Comprehensive representation of a Supabase User.
    This is what the 'protected_path' dependency returns.
    '''

    id: Annotated[
        str,
        Field(
            ...,
            description="Unique UUID for the user in Supabase"
        )
    ]
    aud: Annotated[
        str,
        Field(
            ...,
            description="Audience for the token (usually 'authenticated')"
        )
    ]
    role: Annotated[
        Optional[str],
        Field(
            None,
            description="User's role"
        )
    ]
    email: Annotated[
        Optional[EmailStr],
        Field(
            None,
            description="Registered email address"
        )
    ]
    email_confirmed_at: Annotated[
        Optional[datetime],
        Field(
            None,
            description="Timestamp when the email was confirmed"
        )
    ]
    phone: Annotated[
        Optional[str],
        Field(
            None,
            description="Registered phone number"
        )
    ]
    last_sign_in_at: Annotated[
        Optional[datetime],
        Field(
            None,
            description="Timestamp of the most recent sign-in"
        )
    ]
    app_metadata: Annotated[
        Optional[UserAppMetadata],
        Field(
            None,
            description="System-level metadata (provider, etc.)"
        )
    ]
    user_metadata: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            description="Custom user metadata (name, avatar, etc.)"
        )
    ]
    identities: Annotated[
        Optional[List[UserIdentity]],
        Field(
            None,
            description="List of identities linked to this account"
        )
    ]
    created_at: Annotated[
        datetime,
        Field(
            ...,
            description="User account creation timestamp"
        )
    ]
    updated_at: Annotated[
        datetime,
        Field(
            ...,
            description="Last account update timestamp"
        )
    ]
