import requests
import json
import logging
import threading
import time
from flask import Flask
from db.schema import db, Job
from db.seed import seed_data
from app import app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_flask_app():
    app.run(debug=False, use_reloader=False, port=5000)

def test_workflow():
    # Seed the database and get job_id
    with app.app_context():
        db.create_all()
        seed_data(db)
        job = Job.query.filter_by(title="Software Engineer").first()
        if not job:
            logger.error("Failed to find seeded job")
            return
        job_id = job.id
        logger.info(f"Using seeded job_id: {job_id}")

    # Start Flask app in a separate thread
    threading.Thread(target=run_flask_app, daemon=True).start()

    # Wait for Flask app to start
    time.sleep(2)

    url = "http://127.0.0.1:5000/run_agent"
    input_data = {
        "job_id": job_id,
        "title": "Software Engineer",
        "description": "Develop web applications using Python and Flask.",
        "requirements": ["Python", "Flask", "SQLAlchemy"],
        "role": "Hiring Manager"
    }

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=input_data, timeout=10)
            response.raise_for_status()
            result = response.json()
            logger.info("Workflow Result:")
            logger.info(json.dumps(result, indent=2))
            break
        except requests.exceptions.RequestException as e:
            logger.error(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt == max_retries - 1:
                logger.error("Max retries reached. Workflow failed.")
                return
            time.sleep(2)

if __name__ == "__main__":
    test_workflow()