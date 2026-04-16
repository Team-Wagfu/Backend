from fastapi import APIRouter
from pydantic import Field
from typing import Annotated
from .. import env

router = APIRouter(
	prefix='/test',
	tags=['test'],
)

@router.get(
	'/env_variables'
)
async def return_env_variables():
	return env

@router.get(
	'/get-something'
)
async def return_something():
	return {
		'value': 'something'
	}

@router.get(
	'/get-value'
)
async def return_something_else(
	value: Annotated[
		int,
		Field(
			default=1
		)
	]
):
	return {
		'passed':value
	}

