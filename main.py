import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)