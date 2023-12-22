import array
def get_list_from_array(array):
        return array.tolist()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)