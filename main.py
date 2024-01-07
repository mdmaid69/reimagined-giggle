import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)