from functools import lru_cache
from dotenv import load_dotenv
from os import getenv


# use lru cache to avoid execution whener an import is initiated
# preserves the variables fetched, in the first call
@lru_cache
def env():
	# load variables from .env file
	load_dotenv()
	
	return {
		"jwt_public_key": getenv("JWT_PUBLIC_KEY"),
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