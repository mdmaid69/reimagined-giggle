import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)