import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)