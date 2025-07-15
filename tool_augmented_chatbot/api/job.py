# chatbot3/api/job.py

from flask import Blueprint, request, jsonify
from database import db
from models import Job

job_bp = Blueprint('job', __name__)

@job_bp.route('/create', methods=['POST'])
def create_job():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    requirements = data.get('requirements')

    job = Job(title=title, description=description, requirements=requirements)
    db.session.add(job)
    db.session.commit()

    return jsonify({"message": "Job created", "id": job.id})

@job_bp.route('/', methods=['GET'])
def list_jobs():
    jobs = Job.query.all()
    return jsonify([{"id": j.id, "title": j.title, "description": j.description, "requirements": j.requirements} for j in jobs])
