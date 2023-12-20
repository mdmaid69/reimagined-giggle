def find_unique_words(sentence):
        return set(sentence.split())
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))