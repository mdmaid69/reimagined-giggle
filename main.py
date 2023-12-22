import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)