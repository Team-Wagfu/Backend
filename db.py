import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

url = os.environ.get("SUPABASE_URL", None)
key = os.environ.get("SUPABASE_KEY", None)

