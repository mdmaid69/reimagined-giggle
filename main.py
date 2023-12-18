import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
x = 10
y = 20
print("Sum:", x + y)