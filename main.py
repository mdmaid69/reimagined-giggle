def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)