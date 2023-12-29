import collections
def create_queue():
        return collections.deque()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)