import praw
import os
import logging
from dotenv import load_dotenv

load_dotenv('.env.local')


# ogging to see when the API is called
logging.basicConfig(level=logging.INFO)

# these are stored in .env
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

def fetch_test_pennystocks_posts():
    """Fetch a non-stickied post from r/pennystocks (hot section)."""
    logging.info("Fetching test posts from r/pennystocks (hot section)...")
    subreddit = reddit.subreddit("pennystocks")
    
    posts = []
    # Increase the limit so that we can filter out stickied posts
    for post in subreddit.hot(limit=10):
        # Skip community highlight or sticky posts
        if post.stickied:
            continue
        posts.append({
            "id": post.id,
            "title": post.title,
            "url": post.url,
            "created_utc": post.created_utc,
            "score": post.score,
            "num_comments": post.num_comments,
            "permalink": post.permalink
        })
        # stop once we have at least 1 post for testing change 1 to different num fi want more
        if len(posts) >= 1:
            break

    logging.info(f"Fetched {len(posts)} non-stickied post(s) successfully!")
    return posts


def fetch_post_comments(post_id):
   
   #top-level comments reddit bot comments havent get removed accully user bots
    
    logging.info(f"Fetching comments for post ID: {post_id}")
    submission = reddit.submission(id=post_id)
    # most recentcomments
    submission.comments.replace_more(limit=0)
    
    comments_data = []
    for comment in submission.comments:
        # skip AutoModerator comments this is the bot comment that is always there on a post
        if comment.author and comment.author.name == "AutoModerator":
            continue

        comments_data.append({
            "body": comment.body,
            "score": comment.score
        })
    
    logging.info(f"Fetched {len(comments_data)} comments for post ID: {post_id}")
    return comments_data
