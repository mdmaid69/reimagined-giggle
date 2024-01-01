import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)