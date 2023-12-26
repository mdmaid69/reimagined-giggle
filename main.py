import shutil
def delete_directory(path):
        shutil.rmtree(path)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))