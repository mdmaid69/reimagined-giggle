import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)