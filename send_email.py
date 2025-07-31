#!/usr/bin/env python3

import smtplib
import ssl
import glob
import os
from email.message import EmailMessage
from datetime import datetime

# Get today's date
date_today = datetime.now().strftime("%Y-%m-%d")

# Email account credentials
sender_email = "your gmail address here"  # Replace with your email
# If using Gmail, you may need to set up an App Password if 2FA is enabled
sender_password = "your google app password here"  # Use an App Password if 2FA is enabled 
receiver_email = "devopsaws804@gmail.com"

# CSV folder path
csv_folder = "/home/ishaq/ansible-practice/csv/" #change path as needed
csv_files = glob.glob(os.path.join(csv_folder, "*.csv"))

# Check if any files found
if not csv_files:
    print("No CSV files found to attach.")
    exit(1)

subject = "Daily System Report - " + date_today
body = """
Dear [Manager's Name],

Please find attached the daily system health reports in CSV format for your review.

Let me know if you have any questions or need further details.

Best regards,  
Muhammad Ishaq  
DevOps Engineer
From Automation Department
"""

# Create email
msg = EmailMessage()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.set_content(body)

# Attach each CSV file
for file_path in csv_files:
    with open(file_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(file_path)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# Send email
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.send_message(msg)

print("Email sent successfully with", len(csv_files), "CSV file(s) attached.")
