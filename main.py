import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)