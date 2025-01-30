from flask import Flask, jsonify
from flask_cors import CORS
from reddit_api import fetch_test_pennystocks_posts

app = Flask(__name__)
CORS(app)

@app.route('/api/reddit', methods=['GET'])
def get_reddit_posts():
    """Fetch a small number of test posts from r/pennystocks (free-tier safe)."""
    posts = fetch_test_pennystocks_posts()
    return jsonify({"status": "success", "data": posts})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
