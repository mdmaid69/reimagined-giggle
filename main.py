def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)