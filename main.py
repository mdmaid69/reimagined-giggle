import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))