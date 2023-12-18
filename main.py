import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import logging
def setup_logging(level):
        logging.basicConfig(level=level)