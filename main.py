  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)