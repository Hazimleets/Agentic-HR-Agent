# chatbot3/api/candidate.py

from flask import Blueprint, request, jsonify
from database import db
from models import Candidate

candidate_bp = Blueprint('candidate', __name__)

@candidate_bp.route('/shortlist', methods=['POST'])
def shortlist_candidate():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    resume_link = data.get('resume_link')
    job_id = data.get('job_id')

    candidate = Candidate(
        name=name,
        email=email,
        resume_link=resume_link,
        job_id=job_id
    )
    db.session.add(candidate)
    db.session.commit()

    return jsonify({
        "message": "Candidate shortlisted",
        "id": candidate.id
    })

@candidate_bp.route('/', methods=['GET'])
def list_candidates():
    candidates = Candidate.query.all()
    return jsonify([
        {
            "id": c.id,
            "name": c.name,
            "email": c.email,
            "resume_link": c.resume_link,
            "job_id": c.job_id
        } for c in candidates
    ])
