import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)