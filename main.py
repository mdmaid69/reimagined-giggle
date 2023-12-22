import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)