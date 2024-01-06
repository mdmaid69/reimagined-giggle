import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import collections
def create_ordered_dict():
        return collections.OrderedDict()