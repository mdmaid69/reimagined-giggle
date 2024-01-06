import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)