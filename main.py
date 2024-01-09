import array
def get_array_typecode(array):
        return array.typecode
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)