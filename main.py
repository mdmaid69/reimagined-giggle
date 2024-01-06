import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)