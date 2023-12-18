import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)