from supabase import create_client, Client
from datetime import datetime
from config import SUPABASE_URL
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve values
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_or_update_ticker(ticker: str, score: float):
    """Insert a new ticker score or update if it exists."""
    try:
        # Check if ticker already exists
        existing = supabase.table("ticker_scores").select("score").eq("id", ticker).execute()
        
        if existing.data:
            # Update existing record
            response = supabase.table("ticker_scores").update({
                "score": score,
                "last_updated": datetime.now().isoformat()
            }).eq("id", ticker).execute()
        else:
            # Insert new record
            response = supabase.table("ticker_scores").insert({
                "id": ticker,
                "score": score,
                "last_updated": datetime.utcnow().isoformat()
            }).execute()
        return response.data
    except Exception as e:
        print(f"Error inserting/updating ticker: {e}")
        return None

def get_top_tickers(limit: int = 10):
    """Retrieve the top N tickers with the highest scores."""
    try:
        response = supabase.table("ticker_scores").select("id, score").order("score", desc=True).limit(limit).execute()
        return response.data
    except Exception as e:
        print(f"Error retrieving top tickers: {e}")
        return None

def get_ticker_score(ticker: str):
    """Retrieve the score of a specific ticker."""
    try:
        response = supabase.table("ticker_scores").select("score").eq("id", ticker).single().execute()
        return response.data["score"] if response.data else 0
    except Exception as e:
        print(f"Error retrieving ticker score: {e}")
        return None
