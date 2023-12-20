import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))