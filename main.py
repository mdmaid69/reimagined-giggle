import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def remove_duplicates(lst):
        return list(set(lst))