import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)