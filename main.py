  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)