import datetime
def get_current_datetime():
        return datetime.datetime.now()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))