from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)  # Define app FIRST
CORS(app)  # Then apply CORS

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "success", "message": "Backend is running"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
