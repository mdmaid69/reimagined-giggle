import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_area_circle(r):
        return 3.14 * r**2