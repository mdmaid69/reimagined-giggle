import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)