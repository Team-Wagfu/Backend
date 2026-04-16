import os
from . import env
from supabase import create_client, Client
from fastapi import HTTPException, status

# Load environment variables
try:
	SUPABASE_URL = env["project_url"]
	SUPABASE_KEY = env["supabase_service_key"]
except Exception as e:
	raise EnvironmentError(f"Failed to load environment variables: {str(e)}")

def get_db() -> Client:
	try:
		con = create_client(
			SUPABASE_URL,
			SUPABASE_KEY
		)
		return con
	except Exception as e:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail=f"Failed to connect to database, {str(e)}",
		)

def close_db(db: Client) -> None:
	db.close()