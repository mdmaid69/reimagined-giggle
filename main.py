import array
def extend_array(array, iterable):
        array.extend(iterable)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)