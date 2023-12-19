import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)