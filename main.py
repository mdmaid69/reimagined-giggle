import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))