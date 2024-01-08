import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import array
def clear_array(array):
        array *= 0