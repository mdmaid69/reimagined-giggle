import os
def get_environment_variable(var):
        return os.getenv(var)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))