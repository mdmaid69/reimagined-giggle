import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)