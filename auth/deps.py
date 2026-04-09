# types
from typing import Annotated
from pydantic import Field
from supabase import Client

# fastapi
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# database
from ..db import get_db, close_db

# env
from . import env

__all__ = []

security_model = HTTPBearer(
	description="JWT token",
	auto_error=True
)

'''
[protected path dependency]
use as dependency to protect paths(endpoints) from unauthorized access

async def endpoint(var: int, user: Annotated[User, Depends(get_current_user)]):
	pass

'''
async def get_current_user(
	credentials: Annotated[
		HTTPAuthorizationCredentials,
		Depends(security_model)
	],
	db: Annotated[Client, Depends(get_db)]
):
	token = credentials.credentials
	scheme = credentials.scheme

	print(f'Authenticating using scheme:{scheme} with token:{token}')

	# try to decode the jwt token
	try:
		response = db.auth.get_user(token)
		if not response.user:
			raise HTTPException(
				status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
				detail="Failed to verify token",
				headers={"WWW-Authenticate": "Bearer"} # include custom header in the resonse
			)

		return response.user
	except Exception as e:
		# invalid token or other excpetion
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Unable to authenticate, token failure",
			headers={"WWW-Authenticate": "Bearer"}
		)


'''
[decode and validate jwt]

'''
def validate_jwt(
	token: Annotated[
		str,
		Field(
			...,
			description="JWT token"
		)
	]
):
	