from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import re

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = 'path_to_your_service_account.json'  # Replace with actual path

def get_appointment_reminders():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials)

    # Get events for tomorrow
    tomorrow = datetime.utcnow() + timedelta(days=1)
    start = datetime(tomorrow.year, tomorrow.month, tomorrow.day)
    end = start + timedelta(days=1)

    events_result = service.events().list(
        calendarId='primary',
        timeMin=start.isoformat() + 'Z',
        timeMax=end.isoformat() + 'Z',
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    reminders = []

    for event in events:
        summary = event.get('summary', '')
        match = re.search(r'-ar\s+([\w\s]+)', summary)
        if match:
            patient_name = match.group(1).strip()
            time = event['start'].get('dateTime', event['start'].get('date'))
            reminders.append({
                'patient': patient_name,
                'time': time
            })

    return reminders
