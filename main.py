import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())