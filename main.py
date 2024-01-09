import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)