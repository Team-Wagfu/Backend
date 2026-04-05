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

@router.post(
	"/",
    dependencies=[Depends(protected_path)]
)
async def append_pet(user: Annotated[any, Depends(protected_path)]):
	# add a new pet using authorized user context
    pass
	