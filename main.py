import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)