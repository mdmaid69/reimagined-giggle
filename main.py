  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)