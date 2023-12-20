import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)