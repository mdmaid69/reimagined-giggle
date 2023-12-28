import array
def check_if_array_contains_item(array, item):
        return item in array
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)