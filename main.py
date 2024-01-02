import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)