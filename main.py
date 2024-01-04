import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))