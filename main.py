import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_area(radius):
        return 3.14 * radius * radius