i = 0
while i < 5:
        print(i)
        i += 1
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)