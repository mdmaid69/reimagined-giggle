text = "Hello, world!"
print("Reversed:", text[::-1])
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)