import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))