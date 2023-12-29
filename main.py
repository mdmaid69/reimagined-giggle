import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)