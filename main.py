import array
def get_array_as_tuple(array):
        return tuple(array)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)