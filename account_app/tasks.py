import smtplib
from celery import shared_task
from odyssey.settings import SENDER_MAIL_ID, SENDER_MAIL_PASSWORD


@shared_task()
def send_mail(receiver_mail, user_message):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(SENDER_MAIL_ID, SENDER_MAIL_PASSWORD)
    s.sendmail(SENDER_MAIL_ID, receiver_mail, user_message)
    s.quit()
