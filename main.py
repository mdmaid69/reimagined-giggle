import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)