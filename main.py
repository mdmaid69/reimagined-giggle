import array
def get_array_as_complex(array):
        return complex(array[0])
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)