import array
def get_array_as_bool(array):
        return bool(array)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)