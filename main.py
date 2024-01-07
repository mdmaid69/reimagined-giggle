import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def is_even(n):
        return n % 2 == 0