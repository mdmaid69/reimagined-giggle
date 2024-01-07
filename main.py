text = "Hello, world!"
print("Uppercase:", text.upper())
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)