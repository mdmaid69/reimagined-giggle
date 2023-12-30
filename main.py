  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)