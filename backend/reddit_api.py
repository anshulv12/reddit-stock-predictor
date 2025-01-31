import praw
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging to see when the API is called
logging.basicConfig(level=logging.INFO)

# Reddit API Credentials (stored in .env)
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

def fetch_test_pennystocks_posts():
    # TODO: Can we filter based on time of post/comment
    """Fetch a small number of posts from r/pennystocks (free-tier safe)."""
    logging.info("Fetching test posts from r/pennystocks...")  # Debugging output
    subreddit = reddit.subreddit("pennystocks")
    
    posts = []
    for post in subreddit.new(limit=2):  # Fetch ONLY 2 posts
        posts.append({
            "title": post.title,
            "url": post.url,
            "created_utc": post.created_utc,
            "score": post.score,
            "num_comments": post.num_comments
        })
    
    logging.info(f"Fetched {len(posts)} posts successfully!")  # Debugging output
    return posts
