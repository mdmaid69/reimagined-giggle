import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)