import math
def calculate_sign(x):
        return math.copysign(1, x)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)