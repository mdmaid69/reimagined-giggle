import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)