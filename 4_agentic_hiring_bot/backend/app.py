from flask import Flask, request, jsonify
from db.schema import db, Job, Candidate
from flask_cors import CORS
from config import Config
from agents.agent import run_agent
from db.seed import seed_data

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    seed_data(db)
    print("Jobs:", Job.query.all())
    print("Candidates:", Candidate.query.all())

@app.route('/')
def index():
    return {"message": "Chatbot 4 Agentic Hiring Bot is running."}

@app.route('/run_agent', methods=['POST'])
def run_agent_route():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    input_data = request.get_json()
    if not input_data:
        return jsonify({"error": "Empty JSON payload"}), 400
    response = run_agent(input_data)
    return jsonify(response)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("✅ Starting Chatbot 4 (Agentic Hiring Bot)")
    app.run(debug=Config.DEBUG)