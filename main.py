import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
for i in range(5):
        print(i)