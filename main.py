import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)