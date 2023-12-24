def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)