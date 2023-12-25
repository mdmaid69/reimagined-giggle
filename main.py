  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)