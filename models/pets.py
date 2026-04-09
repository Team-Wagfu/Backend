from pydantic import BaseModel, Field
from typing import Annotated, List, Union, Dict, Optional
from datetime import date
from uuid import UUID

# self imports
from .enums import PetType, Status, Breed, Colors
from .vaccines import Vaccines

__all__ = [
	"Pet","Pets",
	"PetAddResponse"
]

# base models
class Pet(BaseModel):

	'''
	[[Pet Model]]
	[Example]

	// as per the initial documentation
	{
		"id": "pet_001",
		"passportId": "PW-2024-00142",
		"name": "Luna",
		"type": "Dog",
		"breed": "Golden Retriever",
		"dateOfBirth": "2021-03-15",
		"color": "Golden",
		"weight": 28.5,
		"height": 58,
		"ownerName": "Alex Johnson",
		"healthScore": 87
	}

	// has been corrected of logical errors and changed to
	{
		"pet_id": "PET-2024-12035",
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

	[Description]
	return the pet details concerning a single pet, List[Pet] can be used to
	return the result as multiple related pets.
	'''

	pet_id: Annotated[
		str,
		Field(
			pattern=r"^PET-\d{4}-\d{6}$",
			description="pet id that starts with the characters PET-",
			example="PET-2024-00421"
		)
	]
	name: Annotated[
		str, 
		Field(
			..., 
			min_length=3, 
			max_length=50,
			description="name of the pet",
			example="Doby"
		)
	]
	dob: Annotated[
		date, 
		Field(
			...,
			description="Date of Birth of the pet",
			example="22-03-2015"
		)
	]
	type: Annotated[
		PetType, 
		Field(
			...,
			description="Type of the pet",
			example="Dog, Cat, ..."
		)
	]
	breed: Annotated[
		Union[
			Breed.dog, 
			Breed.cat, 
			Breed.bird,
			Breed.fish, 
			Breed.reptile, 
			Breed.rabbit,
			Breed.other
		], 
		Field(
			..., 
			min_length=3, 
			max_length=50,
			description="A small description of the breed",
			example="Golden retriever"
		)
	]
	color: Annotated[
		Union[
			Colors.dog, 
			Colors.cat, 
			Colors.bird,
			Colors.fish, 
			Colors.reptile, 
			Colors.rabbit,
			Colors.other
		], 
		Field(
			...,
			description="color of the pet",
			example="black"
		)
	]
	weight: Annotated[
		int, 
		Field(
			..., 
			ge=1,
			description="weight of the pet in kg",
			example=32
		)
	]
	height: Annotated[
		int, 	
		Field(
			..., 
			ge=1,
			description="height of pet in cm",
			example=78
		)
	]
	
	vaccines: Annotated[
		Dict[
			date,
			Union[
				Vaccines.dVaccine,
				Vaccines.cVaccine,
				Vaccines.rVaccine,
				Vaccines.bVaccine,
				Vaccines.fVaccine,
			]
		],
		Field(
			default_generator={},
			description="List of vaccines",
			example={date.today(): Vaccines.dVaccine.rabies}
		)
	]

	medical_history: Annotated[
		List[MedicalRecords],
		Field(
			default_generator=[],
			description="List of medical records", 
		)
	]

# corresponding Collection type
class Multiple:
	Pets = Annotated[
		List[Pet]
	]

# response models
class PetResponse:

	'''handle models for all the return types of pet related routes'''

	class PetAddResponse(BaseModel):

		'''return result of pet addition to the db'''

		status: Annotated[
			Literal["success", "error"],
			Field(
				...,
				description="status as if the operation(Addition) completed successfully or halted with error"
			)
		]

		error: Optional[str] # only the firsy encountered error will be returned

	class PetGetResponse(BaseModel):
		pass

	class PetPatchResponse(BaseModel):
		pass

	class PetDeleteResponse(BaseModel):
		pass

