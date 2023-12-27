import smtplib
def send_email(smtp_server, port, username, password, from_addr, to_addr, subject, body):
        with smtplib.SMTP(smtp_server, port) as server:
        server.login(username, password)
        server.sendmail(from_addr, to_addr, f"Subject: {subject}

{body}")
  def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5