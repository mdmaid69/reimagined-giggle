import array
def get_array_as_bytearray(array):
        return bytearray(array)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)