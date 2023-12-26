n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)