import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)