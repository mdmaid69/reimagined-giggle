import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))