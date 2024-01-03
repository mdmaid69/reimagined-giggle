import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
n = 10
print("Square numbers:", [x**2 for x in range(n)])