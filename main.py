import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import array
def iterate_over_array(array):
        for item in array:
        print(item)