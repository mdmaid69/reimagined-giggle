  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)