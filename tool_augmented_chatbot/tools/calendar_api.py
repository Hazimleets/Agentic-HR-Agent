# chatbot3/tools/calendar_api.py
def schedule_interview(candidate_name, email, datetime):
    print(f"Scheduled interview for {candidate_name} at {datetime}. Invitation sent to {email}.")
    return {"status": "scheduled", "calendar": "Google Calendar"}