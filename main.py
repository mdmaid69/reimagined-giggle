import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)