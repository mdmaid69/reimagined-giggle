import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)