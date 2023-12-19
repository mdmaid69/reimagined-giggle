import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_pressure(force, area):
        return force / area