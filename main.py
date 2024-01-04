import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)