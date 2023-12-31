import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)