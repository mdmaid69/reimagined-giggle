import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)