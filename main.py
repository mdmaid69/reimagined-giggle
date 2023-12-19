import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)