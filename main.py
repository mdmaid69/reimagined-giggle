import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)