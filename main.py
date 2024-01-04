  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)