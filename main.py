import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)