import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)