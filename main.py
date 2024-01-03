import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)