from email_sender import EmailSender

# Initialize EmailSender with your credentials
email_client = EmailSender(sender_email="your_email@gmail.com", sender_password="your_app_password")

# Send an email
success = email_client.send_email(
    recipient_email="recipient_email@gmail.com",
    subject="Automated Email",
    body="Hello, this is an automated email sent using Python."
)

if success:
    print("Email sent successfully!")
else:
    print("Failed to send email.")
