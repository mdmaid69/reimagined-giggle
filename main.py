import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_work(force, distance):
        return force * distance