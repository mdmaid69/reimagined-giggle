import glob
def find_files(pattern):
        return glob.glob(pattern)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))