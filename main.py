import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)