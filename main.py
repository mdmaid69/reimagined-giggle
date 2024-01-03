import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)