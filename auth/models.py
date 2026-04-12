## handle models for autherication

from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated

class User(BaseModel):

	'''act as base configuration for all the subsequenct user models'''

	model_config = ConfigDict(
		use_enum_values=True,
		extra='allow'
	)


class CurrentUser(User):

	'''handle response from get_user'''
	pass

class SignInEmail(User):

	'''handle response of user registering with email-id and password'''
	pass