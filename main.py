import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)