import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))