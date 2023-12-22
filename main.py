list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
import smtplib
def send_email(smtp_server, port, username, password, from_addr, to_addr, subject, body):
        with smtplib.SMTP(smtp_server, port) as server:
        server.login(username, password)
        server.sendmail(from_addr, to_addr, f"Subject: {subject}

{body}")