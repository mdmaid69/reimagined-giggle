import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import os
def list_files_in_directory(path):
        return os.listdir(path)