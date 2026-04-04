from fastapi import APIRouter, HTTPException, Path, Body, Query
from pydantic import Annotated, Field
from typing import Dict, List
from ..db import get_db, close_db
from ..models import Pet

router = APIRouter(
	prefix="/pets",
	tags=["pets"],
	summary="Get and post pet data",
	dependecies=[
		Depends(get_db),
	]
)

@router.post(
	"/pets",
)
async def append_pet():
	pass