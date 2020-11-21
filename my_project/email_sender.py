import smtplib
import sys

gmail_username = 'ivaylo.arnd.s@gmail.com'
gmail_password = 'DTGz9tDNx8LM2aa'

# try:
#     with open('password.secret') as f:
#         gmail_password = f.read().strip('\n')
#     with open('email.secret') as f:
#         gmail_username = f.read().strip('\n')
# except FileNotFoundError:
#     pass

if not gmail_username or not gmail_password:
    raise ValueError(f'please fill your email in {__file__} or in email.secret file and password into the same python file or password.secret\n')

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_username, gmail_password)


def send_mail_fancy(message):
    message["Subject"] = "CPU Report Graphic"
    message["From"] = gmail_username
    message["To"] = gmail_username

    server.sendmail(gmail_username, "bogomila1234@abv.bg", message.as_string())


def send_mail_plain(message):
    subject = "CPU Report text"
    message = "Subject: {}\n\n{}".format(subject, message)
    server.sendmail(gmail_username, gmail_username, message)
