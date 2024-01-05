import os
def get_current_working_directory():
        return os.getcwd()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))