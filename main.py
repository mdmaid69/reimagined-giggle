import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
from collections import Counter
print(Counter("hello world"))