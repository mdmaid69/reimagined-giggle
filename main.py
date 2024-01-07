n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)