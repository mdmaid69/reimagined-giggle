import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)