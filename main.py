import array
def convert_array_to_list(array):
        return array.tolist()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)