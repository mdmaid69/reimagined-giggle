import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import array
def convert_array_to_bytes(array):
        return array.tobytes()