import array
def get_array_slice(array, i, j):
        return array[i:j]
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)