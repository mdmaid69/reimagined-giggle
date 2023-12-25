import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)