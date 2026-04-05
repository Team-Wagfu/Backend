import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

def get_supabase_client() -> Client:
    """
    Initializes and returns a Supabase client instance.
    Uses credentials from environment variables:
    - SUPABASE_URL: Your Supabase project URL.
    - SUPABASE_KEY: Your Supabase project API key.
    """
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")

    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables are not set.")

    return create_client(url, key)

# Create a singleton Supabase client
supabase: Client = get_supabase_client()

# Utility to get the supabase instance, can be used as a FastAPI dependency or directly.
def get_db():
    """
    FastAPI dependency that provides the database connection.
    In the context of Supabase, we reuse the singleton client.
    """
    return supabase
