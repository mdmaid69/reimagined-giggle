import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))