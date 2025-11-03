# 📨 Python Twilio WhatsApp Scheduler

A **Python-based automation project** that uses the **Twilio API** to send and schedule **WhatsApp messages** at a specific date and time.  
This tool allows users to compose personalized messages, set delivery time, and automatically send them through WhatsApp — all using Python.

---

## 📖 Project Overview

This project demonstrates how to automate WhatsApp messaging using Python and the **Twilio API**.  
Users can enter the recipient’s details, the message, and the desired date and time — and the script automatically sends the message at the scheduled moment.

This is a great mini-project for **Python beginners** exploring **APIs, automation, and scheduling tasks**.

---

## 💡 Features

✅ Schedule WhatsApp messages for future delivery  
✅ Send personalized messages automatically  
✅ Secure Twilio API integration  
✅ Time-based automation using `datetime` and `time` modules  
✅ Beginner-friendly and easy to customize  

---

## 🧰 Tech Stack

| Component | Description |
|------------|-------------|
| **Language** | Python |
| **Library** | Twilio |
| **Modules Used** | `datetime`, `time` |
| **API** | Twilio WhatsApp Sandbox |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/python-twilio-whatsapp-scheduler.git
cd python-twilio-whatsapp-scheduler


2️⃣ Install Required Packages
pip install twilio

3️⃣ Set Up Twilio WhatsApp Sandbox

1. Go to Twilio Console

2. Activate the WhatsApp Sandbox.

3. Note down your:

Account SID

Auth Token

Twilio Sandbox Number (e.g., +14155238886)

4. Connect your WhatsApp to the Twilio Sandbox (you’ll get a join code like join blue-butterfly).

4️⃣ Update Credentials in the Code

In your Python file, update:
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
```
---

# ▶️ Usage

Run the script:
python whatsapp_scheduler.py

Follow the on-screen instructions:

1. Enter recipient name
2. Enter WhatsApp number (with country code, e.g., +919876543210)
3. Type your message
4. Enter date and time for sending (e.g., 2025-11-03 and 18:30)
5. The program waits until that time and sends the message automatically 🚀

---

# 🧠 Example Output

Enter recipient's name: Aditya
Enter recipient's WhatsApp number with country code (e.g., +1234567890): +919876543210
Enter the message you want to send to Aditya: Hello! This is your scheduled reminder.
Enter the date to send the message (YYYY-MM-DD): 2025-11-04
Enter the time to send the message (HH:MM in 24-hour format): 08:30
✅ Message scheduled to be sent to Aditya at 2025-11-04 08:30. Waiting...
Message sent successfully! Message SID: SMxxxxxxxxxxxxxxxxxxxxxxxxxxxx

---

## 🛡️ Security Note

⚠️ **Important:** The Twilio `Account SID` and `Auth Token` used in this project are sensitive credentials.  
For simplicity, this demo stores them directly in the script — but in real projects, you should **never hardcode credentials**.

✅ Instead, store them securely using **environment variables** or a separate `.env` file.

Example (recommended approach):
```bash
setx TWILIO_ACCOUNT_SID "your_sid"
setx TWILIO_AUTH_TOKEN "your_token"

---
