""" import smtplib
from email.message import EmailMessage
from content import template

smtp_server = "mail.sucresecure.com"
smtp_port = 465

email_emitter = "labsecureemailtest@sucresecure.com"
email_password = "nixcmc6Dkt5Ay2Y"

receiver_email = "joalrope@gmail.com"

message = EmailMessage()

message['Subject'] = "Email de prueba desde Python"
message['From'] = email_emitter
message['To'] = receiver_email

message.set_content(template, subtype="html")

server = smtplib.SMTP_SSL(f'{smtp_server}:{smtp_port}')
server.ehlo()
server.login(email_emitter, email_password)
server.send_message(message)
server.quit()
print("Envio exitoso") """

# import all necessary components
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

smtp_server = "mail.sucresecure.com"
smtp_port = 465

sender_email = "labsecureemailtest@sucresecure.com"

email_password = "nixcmc6Dkt5Ay2Y"
receiver_email = "joalrope@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "CID image test"
message["From"] = sender_email
message["To"] = receiver_email

# write the HTML part
html = """\
<html>
 <body>
   <img src="cid:Mailtrapimage">
 </body>
</html>
"""

part = MIMEText(html, "html")
message.attach(part)

# We assume that the image file is in the same directory that you run your Python script from
fp = open('Escanear.jpeg', 'rb')
image = MIMEImage(fp.read())
fp.close()

# Specify the  ID according to the img src in the HTML part
image.add_header('Content-ID', '<Mailtrapimage>')
message.attach(image)

# send your email
with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(sender_email, email_password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
print('Sent')
