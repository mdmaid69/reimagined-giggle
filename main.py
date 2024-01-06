import array
def get_array_as_list(array):
        return list(array)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)