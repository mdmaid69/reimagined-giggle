  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)