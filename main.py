import array
def get_array_as_memoryview(array):
        return memoryview(array)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)