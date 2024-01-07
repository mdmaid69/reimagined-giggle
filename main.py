import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)