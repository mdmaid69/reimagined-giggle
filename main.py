import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import array
def get_array_length(array):
        return len(array)