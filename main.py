import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable