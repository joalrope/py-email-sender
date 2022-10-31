import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


from templates.content import template


def client_notifs_email(name, receiver_email):

    smtp_server = "mail.sucresecure.com"
    smtp_port = 465

    sender_email = "labsecureemailtest@sucresecure.com"

    email_password = "nixcmc6Dkt5Ay2Y"
    #receiver_email = "joalrope@gmail.com"

    message = MIMEMultipart("alternative")
    message["Subject"] = "CID image test"
    message["From"] = sender_email
    message["To"] = receiver_email

    part = MIMEText(template(name, receiver_email), "html")
    message.attach(part)

    fp = open('user_photo.png', 'rb')
    image = MIMEImage(fp.read())
    fp.close()

    image.add_header('Content-ID', '<Mailtrapimage>')
    message.attach(image)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, email_password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    print('Sent')
