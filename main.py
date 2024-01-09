  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)