import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)