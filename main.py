import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)