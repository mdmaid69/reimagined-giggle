import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import array
def remove_from_array(array, item):
        array.remove(item)