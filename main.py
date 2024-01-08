import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))