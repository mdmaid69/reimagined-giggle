import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))