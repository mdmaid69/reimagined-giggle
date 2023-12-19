import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)