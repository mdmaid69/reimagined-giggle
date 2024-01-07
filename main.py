sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))