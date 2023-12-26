import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)