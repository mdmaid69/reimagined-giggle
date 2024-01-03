import datetime
def get_today_date():
        return datetime.date.today()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))