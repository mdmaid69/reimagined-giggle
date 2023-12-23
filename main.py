import array
def get_array_index(array, item):
        return array.index(item)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)