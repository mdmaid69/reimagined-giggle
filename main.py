n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)