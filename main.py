import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_area_triangle(b, h):
        return 0.5 * b * h