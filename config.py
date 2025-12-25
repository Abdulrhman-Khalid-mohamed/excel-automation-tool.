import os

# Folders
SAMPLE_FOLDER = "sample_data"
OUTPUT_FOLDER = "outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Optional Email Settings
EMAIL_ENABLED = False  # Change to True if you want email notifications
EMAIL_SENDER = "your_email@example.com"
EMAIL_RECEIVER = "receiver_email@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_PASSWORD = "your_email_password"
