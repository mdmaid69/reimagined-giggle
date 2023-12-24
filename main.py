import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))