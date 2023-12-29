import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_speed(distance, time):
        return distance / time