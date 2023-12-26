import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))