from functools import lru_cache
from dotenv import load_dotenv
from os import getenv
from requests import get

# use lru cache to avoid execution whener an import is initiated
# preserves the variables fetched, in the first call
@lru_cache
def env():
	# load variables from .env file
	load_dotenv()
	
	return {
		"jwt_public_key_url": getenv("JWT_PUBLIC_KEY_URL"),
		"jwt_public_key": get(getenv("JWT_PUBLIC_KEY_URL")).json(),
		"jwt_secret": getenv("JWT_SECRET"),
		"jwt_expiry": getenv("JWT_EXPIRY"),
		"project_url": getenv("PROJECT_URL"),
		"postgres_direct": getenv("POSTGRES_DIRECT"),
		"supabase_publishable_key": getenv("SUPABASE_PUBLISHABLE_KEY"),
		"supabase_secret_key": getenv("SUPABASE_SECRET_KEY"),
		"supabase_anon_key": getenv("SUPABASE_ANON_KEY"),
		"supabase_service_key": getenv("SUPABASE_SERVICE_KEY")
	}

__all__ = ["env"]