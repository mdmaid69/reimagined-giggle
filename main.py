def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)