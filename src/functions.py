import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string

# Получаем данные для SMTP сервера
SMTP_HOST = 'smtp.mail.ru'
SMTP_PORT = 465
SMTP_MAIL = 'goha1115@mail.ru'
SMTP_PASSWORD = 'imrxgq0MprMkdm35bcH2'


def send_mail(to_addr, subject, text):
    print('вызов функции send mail')
    """
    Функция для отправки электронных писем.
    """
    # Создаем объект сообщения
    msg = MIMEMultipart()
    msg['From'] = 'goha1115@mail.ru'
    msg['To'] = to_addr
    msg['Subject'] = subject

    # Добавляем текст сообщения
    msg.attach(MIMEText(text, 'plain'))

    # Подключаемся к SMTP серверу и отправляем сообщение
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_MAIL, SMTP_PASSWORD)
        server.send_message(msg)


def generate_password(length):
    """
    Функция для генерации случайного пароля указанной длины.
    """
    # Список возможных символов для пароля
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерируем пароль
    password = ''.join(random.choice(characters) for _ in range(length))

    return password
