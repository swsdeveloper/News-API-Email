import smtplib
from email.message import EmailMessage
import ssl
import os


def send_email_2(subject, message, eml_from="steven.w.shatz@gmail.com", eml_to="sshatz@aesopscorp.com"):
    """
    Send email from and to myself (supports UTF-8 encoding)

    :param subject: Subject of the email
    :param message: The body of the email in which the first line is the subject (str)
    :param eml_from: From email address
    :param eml_to: To email address
    :return: None
    """
    msg = EmailMessage()

    msg.set_content(message)

    msg['Subject'] = subject
    msg['From'] = eml_from
    msg['To'] = eml_to

    eml_host = "smtp.gmail.com"
    eml_port = 465

    # Instead of hardcoding the password, use an Environment Variable (see: ~/.bash_profile)
    eml_from_password = os.getenv("BESTCOPWD")

    eml_context = ssl.create_default_context()  # to send email securely

    with smtplib.SMTP_SSL(host=eml_host, port=eml_port, context=eml_context) as server:
        server.login(eml_from, eml_from_password)
        server.send_message(msg)  # Use this (instead of send_mail) to support UTF8 characters!!!
