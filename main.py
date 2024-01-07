import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()