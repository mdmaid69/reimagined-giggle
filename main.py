import array
def get_array_as_repr(array):
        return repr(array)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)