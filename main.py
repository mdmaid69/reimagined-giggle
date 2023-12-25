import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)