import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)