import os
def get_file_size(filename):
        return os.path.getsize(filename)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))