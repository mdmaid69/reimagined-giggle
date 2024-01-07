import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)