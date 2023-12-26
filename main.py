import array
def convert_array_to_string(array):
        return array.tostring()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)