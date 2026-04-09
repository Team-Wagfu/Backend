'''
Pet handling routes
> Handle pet addition
> Handle pet Deletion
> Handle Pet metadata modification
> Handle pet retrieval
'''

from fastapi import APIRouter, HTTPException, Path, Body, Query, Depends
from pydantic import Annotated, Field
from typing import Dict, List
from ..db import get_db, close_db
from ..models import Pet
from ..auth import protected_path

router = APIRouter(
	prefix="/pets",
	tags=["pets"],
	summary="add and retrieve pet information",
	dependencies=[
		Depends(get_db),
		Depends(protected_path)
	]
)


# Pet Addition
@router.post(
	"/",
	dependencies=[Depends(protected_path)]
)
async def append_pet(
	user: Annotated[
		any, 
		Depends(protected_path)
	]
):
	return user