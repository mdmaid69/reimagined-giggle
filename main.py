import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)