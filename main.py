import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)