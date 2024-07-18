import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, password, subject, message):
  """
  Sends an email using a secure SMTP connection.

  Args:
      sender_email (str): The email address of the sender.
      receiver_email (str): The email address of the recipient.
      password (str): The password for the sender's email account.
      subject (str): The subject of the email.
      message (str): The body of the email.
  """

  # Use a secure SMTP port (587 for Gmail)
  smtp_server = "smtp.gmail.com"
  smtp_port = 587

  # Create a secure connection with STARTTLS
  with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()

    # Login with authentication
    server.login(sender_email, password)

    # Create a MIMEText object for the message
    email_content = MIMEText(message, _subtype='plain')
    email_content['Subject'] = subject
    email_content['From'] = sender_email
    email_content['To'] = receiver_email

    # Send the email
    server.sendmail(sender_email, receiver_email, email_content.as_string())

    print("Email sent successfully!")

# Replace with your actual email credentials
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@example.com"
password = "your_app_password"  # Use app password for Gmail (more secure)
subject = "Secure Python Email with Best Practices"
message = "This is a test email sent using a secure Python script."

send_email(sender_email, receiver_email, password, subject, message)
