import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def divide_numbers(x, y):
        return x / y