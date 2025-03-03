from flask import Flask, jsonify
from flask_cors import CORS
from reddit_api import fetch_test_pennystocks_posts, fetch_post_comments

app = Flask(__name__)
CORS(app) 

@app.route('/api/reddit', methods=['GET'])
def get_reddit_posts():
    #Fetch a 1 test posts from r/pennystocks hot section 
    posts = fetch_test_pennystocks_posts()
    return jsonify({"status": "success", "data": posts})


@app.route('/api/reddit/<post_id>/comments', methods=['GET'])
def get_post_comments(post_id):
   #Fetch comments for a reddit post using the ID
    comments = fetch_post_comments(post_id)
    return jsonify({"status": "success", "data": comments})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
