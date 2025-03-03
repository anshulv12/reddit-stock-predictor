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
    #2 posts from /pennystocks
    logging.info("Fetching test posts from r/pennystocks...")
    subreddit = reddit.subreddit("pennystocks")
    
    posts = []   #this line below is what changes what section so .new is new and .hot is hot
    for post in subreddit.hot(limit=1):  # Fetch only 1 keep it cheap for testing
        posts.append({
            "id": post.id,              
            "title": post.title,
            "url": post.url,
            "created_utc": post.created_utc,
            "score": post.score,
            "num_comments": post.num_comments,
            "permalink": post.permalink
        })
    
    logging.info(f"Fetched {len(posts)} posts successfully!")
    return posts

def fetch_post_comments(post_id):
   
   #Given a Reddit post ID, fetch its top-level comments reddit bot comments havent get removed accully user bots
    
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
