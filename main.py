import math
def calculate_error_function(x):
        return math.erf(x)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)