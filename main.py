import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)