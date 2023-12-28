import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)