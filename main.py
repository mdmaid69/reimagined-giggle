import math
def calculate_absolute_value(x):
        return math.fabs(x)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)