import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array