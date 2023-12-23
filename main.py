import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)