import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)