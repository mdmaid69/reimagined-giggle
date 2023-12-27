import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)