import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)