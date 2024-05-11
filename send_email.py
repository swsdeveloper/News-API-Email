import smtplib
import ssl
import os


def send_email(message):
    """
    Send email to myself containing a user's email address and message.
    This is invoked when user presses "Submit" button on Contact page.

    :param message: The body of the email in which the first line is the subject (str)
    :return: None
    """

    eml_host = "smtp.gmail.com"
    eml_port = 465

    eml_from = "steven.w.shatz@gmail.com"
    eml_to = "sshatz@aesopscorp.com"

    # Instead of hardcoding the password, use an Environment Variable (see: ~/.bash_profile)
    eml_from_password = os.getenv("BESTCOPWD")

    eml_context = ssl.create_default_context()  # to send email securely

    with smtplib.SMTP_SSL(host=eml_host, port=eml_port, context=eml_context) as server:
        server.login(eml_from, eml_from_password)
        server.sendmail(eml_from, eml_to, message)
