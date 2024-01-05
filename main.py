import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))