import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)