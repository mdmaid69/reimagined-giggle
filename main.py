  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)