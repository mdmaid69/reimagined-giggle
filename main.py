def calculate_volume(length, width, height):
        return length * width * height
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)