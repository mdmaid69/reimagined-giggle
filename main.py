import re
def split_string(pattern, string):
        return re.split(pattern, string)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))