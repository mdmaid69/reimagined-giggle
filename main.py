import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)