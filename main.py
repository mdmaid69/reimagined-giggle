import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)