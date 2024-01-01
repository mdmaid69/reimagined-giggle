import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)