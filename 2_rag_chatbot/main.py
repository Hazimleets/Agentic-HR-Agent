from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from rag_app import generate_answer

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "online"})

@app.route('/rag_generate', methods=['POST'])
def rag_generate():
    prompt = request.json.get("prompt")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = generate_answer(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
