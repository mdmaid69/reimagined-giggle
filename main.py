def is_even(n):
        return n % 2 == 0
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)