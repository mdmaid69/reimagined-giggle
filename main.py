import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)