import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)