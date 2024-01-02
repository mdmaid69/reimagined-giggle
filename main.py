import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)