# chatbot3/api/tools.py

from flask import Blueprint, jsonify
from tools.linkedin_api import post_job_to_linkedin
from tools.calendar_api import schedule_interview
from tools.gmail_api import send_email

tools_bp = Blueprint('tools', __name__)

@tools_bp.route('/sync', methods=['GET'])
def sync_tools():
    # You can later call your actual APIs here.
    # For now, mock the behavior.
    return jsonify({
        "linkedin": "LinkedIn sync successful",
        "calendar": "Google Calendar sync successful",
        "gmail": "Gmail API sync successful"
    })
