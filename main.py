import smtplib
def send_email(smtp_server, port, username, password, from_addr, to_addr, subject, body):
        with smtplib.SMTP(smtp_server, port) as server:
        server.login(username, password)
        server.sendmail(from_addr, to_addr, f"Subject: {subject}

{body}")
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")