import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)