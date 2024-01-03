import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
n = 10
print("Powers of 2:", [2**x for x in range(n)])