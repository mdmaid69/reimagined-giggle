import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)