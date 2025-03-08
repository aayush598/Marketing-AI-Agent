import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, sender_email: str, sender_password: str):
        """
        Initialize the email sender with sender credentials.
        :param sender_email: Sender's Gmail address
        :param sender_password: App Password for Gmail authentication
        """
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_email(self, recipient_email: str, subject: str, body: str) -> bool:
        """
        Sends an email using Gmail SMTP.
        :param recipient_email: Receiver's email address
        :param subject: Email subject
        :param body: Email body content
        :return: True if email sent successfully, else False
        """
        try:
            # Set up the email
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            # Connect to the Gmail SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, message.as_string())

            return True

        except Exception as e:
            print(f"Failed to send email: {e}")
            return False


