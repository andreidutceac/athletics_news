import smtplib, ssl
import os

import main
from main import day_articles

articles = main.day_articles


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "fraziermorris39@gmail.com"
    #password = os.getenv("PASSWORD")
    password = "epesvtibriwfyent"

    receiver = "dutceacandrei7@gmail.com"
    receiver2 = username
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

message = ""
for j in range(len(articles)):
    message = message + "\n" + articles[j]["date"] + '\n\n' + articles[j]['title'] + '\n\n' + articles[j]['link'] + '\n\n\n'

if message != "":
    send_email(message)
