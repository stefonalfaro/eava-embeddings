from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import sys

app = Flask(__name__)
modelName = sys.argv[1]
model = SentenceTransformer(modelName)

@app.route('/embed', methods=['POST'])
def embed():
    sentences = request.json['sentences']
    embeddings = model.encode(sentences)
    return jsonify(embeddings.tolist())

if __name__ == '__main__':
    app.run(debug=False, port=5000)