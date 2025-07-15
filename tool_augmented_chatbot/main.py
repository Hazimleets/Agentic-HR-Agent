# chatbot3/main.py

from flask import Flask
from database import db
from api.job import job_bp
from api.candidate import candidate_bp
from api.tools import tools_bp
from api.org import org_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register blueprints
app.register_blueprint(job_bp, url_prefix='/job')
app.register_blueprint(candidate_bp, url_prefix='/candidate')
app.register_blueprint(tools_bp, url_prefix='/tools')
app.register_blueprint(org_bp, url_prefix='/org')

@app.route('/')
def index():
    return {"message": "Chatbot 3 Flask API is running."}

if __name__ == '__main__':
    app.run(debug=True)
