import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)