# chatbot3/api/org.py

from flask import Blueprint, request, jsonify
from models import Organization
from database import db

org_bp = Blueprint('org', __name__)

@org_bp.route('/', methods=['POST'])
def create_organization():
    data = request.get_json()
    try:
        org = Organization(
            name=data['name'],
            mission=data['mission'],
            vision=data['vision'],
            tech_stack=data['tech_stack'],
            hiring_guidelines=data['hiring_guidelines'],
            onboarding_process=data['onboarding_process']
        )
        db.session.add(org)
        db.session.commit()
        return jsonify({
            "message": "Organization created successfully",
            "organization_id": org.id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@org_bp.route('/', methods=['GET'])
def get_organization():
    org = Organization.query.first()
    if not org:
        return jsonify({"error": "No organization found"}), 404

    return jsonify({
        "id": org.id,
        "name": org.name,
        "mission": org.mission,
        "vision": org.vision,
        "tech_stack": org.tech_stack,
        "hiring_guidelines": org.hiring_guidelines,
        "onboarding_process": org.onboarding_process
    }), 200
