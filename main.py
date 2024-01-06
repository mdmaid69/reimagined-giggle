import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)