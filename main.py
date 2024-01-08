import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h