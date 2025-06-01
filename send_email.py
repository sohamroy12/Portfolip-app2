import smtplib, ssl
import os

# Send email from a function.
def send_email(message):
    email_address = os.getenv("personalEmail_ID")
    email_password = os.getenv("app_emailPASSWORD")
    host = "smtp.gmail.com"
    port = 465
    my_context = ssl.create_default_context()
    receiver = os.getenv("personalEmail_ID")

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(email_address, email_password )
        server.sendmail(from_addr=email_address, to_addrs=receiver, msg=message)
        server.close()