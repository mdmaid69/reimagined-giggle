import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)