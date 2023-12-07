import json
from flask import Flask, abort, request, jsonify
from sentence_transformers import SentenceTransformer
import sys

def load_config():
    try:
        with open('config/config.json', 'r') as config_file:
            config = json.load(config_file)
        return config
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error loading configuration file.")
        sys.exit(1)

app_config = load_config()
api_key = app_config.get('apikey')

def validate_token():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
        if token == api_key:
            return True
    return False

app = Flask(__name__)
modelName = sys.argv[1]
model = SentenceTransformer(modelName)

@app.route('/embed', methods=['POST'])
def embed():
    if not validate_token():
        abort(401)  # Unauthorized access

    if 'sentences' not in request.json:
        abort(400, description="Invalid request format.")

    sentences = request.json['sentences']
    embeddings = model.encode(sentences)
    return jsonify(embeddings.tolist())

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)