import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)