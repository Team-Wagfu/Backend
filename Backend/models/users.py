'''
Model configurations of users, various types of users
Contains models for:
- User
- Pet Owner
- Emergency
- Doctor
- Admin
- Pharmaceutical

Operational Context:
- Request (GET)
- Response (POST)
'''


# imports
from pydantic import BaseModel, Field, Annotated, ConfigDict
from typing import List, Union, Dict
from uuid import UUID

# self imports
from ..extra.enums import UserType, Status
from ..extra.custom_types import IDs, Location, Phone


# User model
class User(BaseModel):

	'''
	[Example]

	{
		"user_id": "123e4567-e89b-12d3-a456-426614174000",
		"type": "doctor",
		"display_name": "Dr. Smith"
	}

	[Description]
	Return the user details concerning a single user, List[User] can be used to
	return the result as multiple related users.
	'''

	user_id: Annotated[
		UUID,
		Field(
			...,
			description="User uuid referenced from the auth"
		)
	]

	type: Annotated[
		UserType,
		Field(
			...,
			description="Type of the user",
		)
	]

	display_name: Annotated[
		str,
		Field(
			...,
			description="display name for the user",
			min_length=3,
			max_length=50,
			example="Dr. Smith"
		)
	]

# pet owner model
class PetOwnerUser(BaseModel):
	user_id: Annotated[
		UUID,
		Field(
			...,
			description="uuid of the user referenced from the auth"
		)
	]

	owner_id: Annotated[
		IDs.PetOwnerID,
		Field(
			...,
			description="Pet owner id",
			example="PW-2024-00001"
		)
	]

	location: Annotated[
		Union[Location.GeoLocation, Location.Address],
		Field(
			...,
			description="Location of the pet owner",
			example={
				"lat": 12.9716,
				"lng": 77.5946
			}
		)
		# will be used with other functionsalities to retrieve the address 
		# from the geocoordinates and validate the address logically
		# TODO
	]

	pet_ids: Annotated[
		List[IDs.PetID],
		Field(
			...,
			description="List of pet ids"
		)
	]

# Emergency contact
class EmergencyUser(BaseModel):

	user_id: Annotated[
		UUID,
		Field(
			...,
			description="uuid of the user referenced from the auth"
		)
	]

	eme_id: Annotated[
		IDs.EmergencyUserID,
		Field(
			...,
			description="User id particular to emergency users",
			example="EME-2024-00001"
		)
	]

	contact: Annotated[
		Phone.PhoneNumber,
		Field(
			...,
			description="phone number, indian format",
			examples=["9876543210", "09876543210", "+919876543210"]
		)
	]

	vehicle_type: Annotated[
		Vehicle.VehicleType,
		Field(
			...,
			description="Type of the vehicle",
			example="ambulance"
		)
	]

	vehicle_reg_no: Annotated[
		Vehicle.VehicleNumber,
		Field(
			...,
			dedscription="Vehicle registration number",
			example="MH02CL0555"
		)
	]

	vehicle_capacity: Annotated[
		Vehicle.VehicleCapacityMetrics,
		Field(
			...,
			description="Capacity of the vehicle",
			example={
				"Dimensions": {
					"height": 1.0,
					"width": 1.0,
					"length": 1.0
				},
				"Weight": 1.0
			}
		)
	]

	user_liscence: Annotated[
		str,
		Field(
			...,
			description="License number of the user",
			example="1234567890"
		)
	]