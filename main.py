import collections
def create_counter():
        return collections.Counter()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)