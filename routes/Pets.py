'''
Pet handling routes
> Handle pet addition
> Handle pet Deletion
> Handle Pet metadata modification
> Handle pet retrieval
'''


# TODO
# integrate protected path with all the relevant accesspoints
# and set up accessing and insertion of data 
# based off the uuid and other identifications


__all__ = ["router"]

# api
from fastapi import APIRouter, HTTPException, Path, Body, Query, Depends

# typing
from pydantic import Field
from typing import Dict, List, Union, Annotated

# db
from supabase import Client
from ..db import get_db, close_db

# types
from ..models.pets import Pet, PetResponse, PetRequest, Multiple
from ..extra.custom_types import IDs

router = APIRouter(
	prefix="/pets",
	tags=["pets"],
	dependencies=[
		Depends(get_db),
	]
)

'''
@get_pet
fetch one or more pets based on the pet id

[Example]

// single pet
GET /pets?pet_id=PET-2024-000001

// multiple pets
GET /pets?pet_id=PET-2024-000001,PET-2024-000002

[Response]

[[Success]]
{
	"status": "success",
	"data": [
		{
			"pet_id": "PET-2024-000001",
			"name": "Doby",
			"dob": "2021-03-15",
			"type": "dog",
			"breed": "Golden Retriever",
			"color": "Golden",
			"weight": 50,
			"height": 59,
			"vaccines": {},
			"medical_history": {}
		}
	],
	"count": 1
}

[[Error]]
{
	"status":"error",
	"error":"<error message>"
}

'''

@router.get(
	'/pets',
	response_model=PetResponse.PetGetResponse,
	summary="retrieve pet information, single/multiple pets based on id",
)
async def get_pet(
	pet_id: Annotated[
		Union[List[IDs.PetID], IDs.PetID],
		Field(..., description="pet id")
	],

	count: Annotated[
		int,
		Field(
			default=1,
			description="number of pets to retrieve, defaults to 1"
		)
	],

	db: Annotated[
		Client,
		Depends(get_db)
	]
):

	# identify the parameter, single/multiple
	if isinstance(pet_id, List):
		
		data : Multiple.Pets = []
		count : int = 0

		# retrieve multiple pets
		for pet in pet_id:

			# if something wrong with the type, halt
			if not isinstance(pet, IDs.PetID):
				return PetResponse.PetGetResponse(
					status="error",
					error="Invalid pet id"
				)

			# fetch the corresponding pet data
			response = db.table('pets').select('*').eq('pet_id', pet).execute()

			## response.data : List[Dict[str,Any]]

			# if successfully fetched, then add the record to data, else raise Exception
			if response.data:
				data.extend(response.data)
				count+=1
			
			else:
				return PetResponse.PetGetResponse(
					status="error",
					error=f"Pet with id {pet} not found, fetched {count} pets"
				)
	
	elif isinstance(pet_id, IDs.PetID):
		
		response = db.table('pets').select('*').eq('pet_id', pet_id).execute()

		if response.data:
			data.extend(response.data)
			count+=1
		
		elif response.error:
			return PetResponse.PetGetResponse(
				status="error",
				error=f"Failed to retrieve pet with id {pet_id}"
			)
	
	# return the fetched result
	return PetResponse.PetGetResponse(
		data=data,
		count=count,
	)

'''
@add_pet
add one or more pets, passed as Pet structures in Body

[Example]

POST /pets
{
	"data": [
		{
			"name": "Doby",
			"dob": "2021-03-15",
			"type": "dog",
			"breed": "Golden Retriever",
			"color": "Golden",
			"weight": 50,
			"height": 59,
			"vaccines": {},
			"medical_history": {}
		}
	]
}

[Response]

[[Success]]
{
	"status": "success",
	"data": [
		{
			"pet_id": "PET-2024-000001",
			"name": "Doby",
			"dob": "2021-03-15",
			"type": "dog",
			"breed": "Golden Retriever",
			"color": "Golden",
			"weight": 50,
			"height": 59,
			"vaccines": {},
			"medical_history": {}
		}
	],
	"count": 1
}

[[Error]]
{
	"status":"error",
	"error":"<error message>"
}

'''

## TODO handle error returns
@router.post(
	'/pets',
	summary="Add one or more pets",
	response_model=PetResponse.PetAddResponse,
)
async def add_pet(
	data: Annotated[
		PetRequest.PetAddRequest,
		Body(
			..., 
			embed=True, 
			description="Pet data, list of pet objects or a single pet object."
		)
	],

	db: Annotated[
		Client,
		Depends(get_db)
	]
):

	# keep track of the number of pets added
	count: int = 0

	if isinstance(data.data, List):
		
		# convert the list of data
		formatted_data = [
			{
				'pet_id':x.pet_id,
				'name':x.name,
				'dob':x.dob,
				'type':x.type,
				'breed':x.breed,
				'color':x.color,
				'weight':x.weight,
				'height':x.height,
				'vaccines':x.vaccines,
				'medical_history':x.medical_history
			}
			for x in data.data
		]

		response = db.table('pets').insert(formatted_data).execute()

		if response.data:
			# data successfully inserted
			count += len(response.data)

	else:

		data: Pet = data.data

		# handle single pet addition
		formatted_data = {
			'pet_id': data.pet_id,
			'name': data.name,
			'dob': data.dob,
			'type': data.type,
			'breed': data.breed,
			'color': data.color,
			'weight': data.weight,
			'height': data.height,
			'vaccines': data.vaccines,
			'medical_history': data.medical_history
		}

		response = db.table('pets').insert(formatted_data).execute()

		if response.data:
			count += 1

	return PetResponse.PetAddResponse(
		count=count,
	)


'''
@delete_pet
delete one or more pets based on the pet id

[Example]

DELETE /pets
{
	"ids": [
		"PET-2024-000001",
		"PET-2024-000002"
	]
}

[Response]

[[Success]]
{
	"status": "success",
	"count": 2
}

[[Error]]
{
	"status":"error",
	"count":0,
	"error":"<error message>"
}

'''
@router.delete(
	'/pets',
	response_model=PetResponse.PetDeleteResponse,
	summary="Delete one or more pets",
)
async def delete_pet(
	data: Annotated[
		PetRequest.PetDeleteRequest,
		Body(
			...,
			embed=True,
			description="List of pet ids to be deleted"
		)
	],

	db: Annotated[
		Client,
		Depends(get_db)
	]
):

	count: int = 0

	if isinstance(data.ids, List):
		
		# list of ids passed
		response = db.table('pets').delete().in_("pet_id",data.ids).execute()
	
	elif isinstance(data.ids, IDs.PetID):

		# single id passed
		response = db.table('pets').delete().eq('pet_id',data.ids).execute()
		count+=1

	if response.data:
		return PetResponse.PetGetResponse(
			count=count
		)
	else: # assume error if data attribute not found
		return PetResponse.PetGetResponse(
			status="error",
			error=f"Failed to delete single record {data.ids}"
		)
