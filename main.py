import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)