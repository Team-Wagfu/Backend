from pydantic import AfterValidator
from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated, List, Union, Dict, Optional, Literal
from datetime import date
from uuid import UUID

# self imports
from ..extra.enums import PetType, Breed, Colors, Vaccines
from ..extra.custom_types import IDs

__all__ = [
	"Pet",				# base model
	"Multiple",			# models for multiple pets(grouped items)
	"PetResponse", 		# models for response
	"PetRequest", 		# models for request
]

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

# base models
class Pet(BaseModel):

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
			default_factory=dict,
			description="List of vaccines",
			example={date.today(): Vaccines.dVaccine.rv}
		)
	]

	medical_history: Annotated[
		List[IDs.MedicalRecordID],
		Field(
			default_factory=list,
			description="List of medical records", 
		)
	]

# corresponding Collection type
class Multiple:
	Pets = Annotated[
		List[Pet],
		AfterValidator(lambda x: x if isinstance(x, Pet) else None)
	]


class PetBase(BaseModel):
	model_config = ConfigDict(
		use_enum_values=True,
		extra="forbid"
	)

	status: Annotated[
		Literal["success","error"],
		Field(
			default="success",
			description="status of the request/response"
		)
	]

	error: Annotated[
		str,
		Field(
			None,
			description="descrvibe the error, if an error has occured"
		)
	]


# response models
class PetResponse:

	'''handle models for all the return types of pet related routes'''

	class PetAddResponse(PetBase):

		'''return result of pet addition to the db'''

		count: Annotated[
			int,
			Field(
				default=0,
				description="return the number of records successfully added",
				ge=0
			)
		]

	class PetGetResponse(PetBase):

		''' return the pet details concerning a single pet, List[Pet] can be used to
		return the result as multiple related pets.
		'''

		data: Annotated[
			Multiple.Pets,
			Field(
				default_factory=[],
				description="List of pets, can be one or multiple"
			)
		]

		count: Annotated[
			int,
			Field(
				default=0,
				ge=0,
				description="number of pets returned"
			)
		]

	class PetPatchResponse(PetBase):

		'''return response of updating/pathing the metadata of a pet'''

		pass

	class PetDeleteResponse(PetBase):

		''' response for deleting a pet'''

		count: Annotated[
			int,
			Field(
				default=0,
				description="return the number of records successfully deleted",
				ge=0
			)
		]


class PetRequest:

	'''handle models for all the put/patch/post requests'''

	class PetAddRequest(PetBase):

		''' new pet has been added'''

		data: Annotated[
			Union[
				Pet,
				Multiple.Pets
			],
			Field(
				...,
				embed=True,
				description="Pet data, list of pet objects or a single pet object."
			)
		]

		count: Annotated[
			int,
			Field(
				default=0,
				ge=0,
				description="number of recordcs being embedded"
			)
		]

	class PetDeleteRequest(PetBase):

		''' the corresponding user has been removed, churned'''

		ids: Annotated[
			Union[
				IDs.PetID,
				List[IDs.PetID]
			],
			Field(
				...,
				embed=True,
				description="List of pet ids to be deleted"
			)
		]

		count: Annotated[
			int,
			Field(
				default=0,
				ge=0,
				description="number of ids, that is being passed on"
			)
		]

	class PetPatchRequest(PetBase):

		''' pet metadata update'''

		pass
