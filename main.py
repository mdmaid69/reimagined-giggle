import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)