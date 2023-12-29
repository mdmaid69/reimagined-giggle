import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height