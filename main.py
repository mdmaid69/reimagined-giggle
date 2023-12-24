import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)