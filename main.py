import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)