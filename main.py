  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)