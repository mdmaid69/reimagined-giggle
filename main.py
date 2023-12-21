import array
def get_array_item(array, i):
        return array[i]
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)