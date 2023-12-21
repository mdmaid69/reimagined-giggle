print(sum(range(10)))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)