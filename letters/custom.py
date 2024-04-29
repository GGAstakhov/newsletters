import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SMTP_HOST = 'smtp.mail.ru'
SMTP_PORT = 465
SMTP_MAIL = 'goha1115@mail.ru'
SMTP_PASSWORD = 'imrxgq0MprMkdm35bcH2'


def send_mail():
    to_addr = 'goha1115@mail.ru'
    subject = 'Привет!'
    text = 'Текст пришёл'

    msg = MIMEMultipart()
    msg['From'] = 'goha1115@mail.ru'
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_MAIL, SMTP_PASSWORD)
        server.send_message(msg)


send_mail()
