import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)