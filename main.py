import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import os
print(os.getcwd())