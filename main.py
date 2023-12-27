import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_perpetuity(payment, rate):
        return payment / rate