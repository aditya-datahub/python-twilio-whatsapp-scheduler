# Step 1 - Install required packages
# pip install twilio

from twilio.rest import Client
from datetime import datetime
import time

# Step 2 - Twilio credentials (keep these secret, never share publicly)
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'

client = Client(account_sid, auth_token)

# Step 3 - Define send message function
def send_whatsapp_message(recipient_number, message_body):
    """Send a WhatsApp message using Twilio API."""
    try:
        message = client.messages.create(
            from_='whatsapp:+1415XXXXXXXX',  # Twilio sandbox number
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'An error occurred while sending the message: {e}')

# Step 4 - Get user input
name = input("Enter recipient's name: ").strip()
recipient_number = input("Enter recipient's WhatsApp number with country code (e.g., +1234567890): ").strip()
message_body = input(f"Enter the message you want to send to {name}: ").strip()

# Step 5 - Get date/time input and calculate delay
date_str = input("Enter the date to send the message (YYYY-MM-DD): ").strip()
time_str = input("Enter the time to send the message (HH:MM in 24-hour format): ").strip()

try:
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
    current_datetime = datetime.now()
    time_difference = schedule_datetime - current_datetime
    delay_seconds = time_difference.total_seconds()

    if delay_seconds <= 0:
        print("❌ The scheduled time is in the past. Please enter a future date and time.")
    else:
        print(f'✅ Message scheduled to be sent to {name} at {schedule_datetime.strftime("%Y-%m-%d %H:%M")}. Waiting...')

        # Step 6 - Wait until the scheduled time
        time.sleep(delay_seconds)

        # Step 7 - Send the message
        send_whatsapp_message(recipient_number, message_body)

except ValueError:
    print("❌ Invalid date or time format. Please use YYYY-MM-DD and HH:MM (24-hour format).")
except Exception as e:
    print(f'⚠️ Unexpected error: {e}')
