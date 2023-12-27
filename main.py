import os
def change_working_directory(path):
        os.chdir(path)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))