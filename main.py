import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))