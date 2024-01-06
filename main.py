import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)