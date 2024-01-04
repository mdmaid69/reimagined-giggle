import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)