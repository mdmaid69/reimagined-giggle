import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)