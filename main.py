import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time