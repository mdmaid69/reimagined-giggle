import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import math
def calculate_logarithm_base_2(x):
        return math.log2(x)