import sys
print(sys.version)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)