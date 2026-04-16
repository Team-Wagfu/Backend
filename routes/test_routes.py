from fastapi import APIRouter
from . import env

router = APIRouter(
	prefix='/test',
	tags=['test'],
)

@router.get(
	'/env_variables'
)
async def return_env_variables():
	return env