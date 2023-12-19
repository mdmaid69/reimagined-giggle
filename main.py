import array
def get_array_as_float(array):
        return float(array[0])
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)