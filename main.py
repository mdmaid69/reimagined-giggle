import math
def calculate_circle_area(radius):
        return math.pi * radius**2
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)