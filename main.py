import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def find_min(lst):
        return min(lst)