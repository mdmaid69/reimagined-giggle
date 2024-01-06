import collections
def create_stack():
        return collections.deque()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)