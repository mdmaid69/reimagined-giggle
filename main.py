import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)