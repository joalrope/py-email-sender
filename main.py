import smtplib
import ssl
from email.message import EmailMessage

email_subject = "Email de prueba desde Python"
sender_email_address = "labsecureemailtest@sucresecure.com"
receiver_email_address = "joalrope@gmail.com"
email_smtp = "mail.sucresecure.com"
email_password = "nixcmc6Dkt5Ay2Y"

# Create an email message object
message = EmailMessage()

# Configure email headers
message['Subject'] = email_subject
message['From'] = sender_email_address
message['To'] = receiver_email_address

# Set email body text
message.set_content("Hello from Python!")

# Set smtp server and port
server = smtplib.SMTP_SSL('mail.sucresecure.com:465')

# Identify this client to the SMTP server
server.ehlo()

# Login to email account
server.login(sender_email_address, email_password)

# Send email
server.send_message(message)

# Close connection to server
server.quit()

print("exito")
