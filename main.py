text = "Hello, world!"
print("Characters:", len(text))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)