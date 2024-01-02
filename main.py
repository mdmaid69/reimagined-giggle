import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)