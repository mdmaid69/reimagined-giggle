import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import time
print(time.time())