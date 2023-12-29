import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_acceleration(speed, time):
        return speed / time