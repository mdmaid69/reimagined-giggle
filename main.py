import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)