import array
def get_string_from_array(array):
        return array.tobytes()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)