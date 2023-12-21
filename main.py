import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)