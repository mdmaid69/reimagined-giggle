import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)