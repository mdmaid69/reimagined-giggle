import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)