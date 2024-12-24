import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
sender_email = "shepa22ece@cmrit.ac.in"
sender_password = "cmrit@123"
receiver_email = "recipient@example.com"  # Replace with the recipient's email

# Email content
subject = "Test Email"
body = "This is a test email sent using Python."

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the body to the email
message.attach(MIMEText(body, "plain"))

# Send the email
try:
    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Update for your SMTP server
        server.starttls()  # Start TLS encryption
        server.login(sender_email, sender_password)  # Login to the server
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
