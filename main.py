import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)