import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)