from calendar_reader import get_appointment_reminders
from whatsapp_sender import send_whatsapp_message
import os

TO_WHATSAPP = os.getenv('TO_WHATSAPP')  # Your verified number

def main():
    reminders = get_appointment_reminders()
    for reminder in reminders:
        message = (
            f"📅 *Appointment Reminder*\n"
            f"👤 Patient: {reminder['patient']}\n"
            f"🕒 Time: {reminder['time']}"
        )
        sid = send_whatsapp_message(TO_WHATSAPP, message)
        print(f"Sent message SID: {sid}")

if __name__ == '__main__':
    main()
