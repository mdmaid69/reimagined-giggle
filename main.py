import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))