import array
def set_array_item(array, i, item):
        array[i] = item
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)