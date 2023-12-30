import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
for i in range(10): print(i)