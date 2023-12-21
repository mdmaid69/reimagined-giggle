import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)