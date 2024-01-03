import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)