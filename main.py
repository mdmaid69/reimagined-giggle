import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)