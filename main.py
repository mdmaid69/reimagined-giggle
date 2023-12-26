import array
def get_array_itemsize(array):
        return array.itemsize
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)