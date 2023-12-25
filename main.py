import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)