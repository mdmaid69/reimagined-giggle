import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))