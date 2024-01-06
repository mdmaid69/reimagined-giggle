import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import smtplib
def send_email(smtp_server, port, username, password, from_addr, to_addr, subject, body):
        with smtplib.SMTP(smtp_server, port) as server:
        server.login(username, password)
        server.sendmail(from_addr, to_addr, f"Subject: {subject}

{body}")