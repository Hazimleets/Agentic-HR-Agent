from flask import Blueprint, request, jsonify
from model import query_llm
from logger import log_request

generate_bp = Blueprint('generate', __name__)

@generate_bp.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt")
    model = data.get("model", "")  # model is optional now, just for logging

    log_request(prompt, model)
    output = query_llm(prompt)  # Always uses local model
    return jsonify({"response": output})
