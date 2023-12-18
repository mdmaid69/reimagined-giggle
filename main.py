import math
def calculate_factorial(n):
        return math.factorial(n)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)