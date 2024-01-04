def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)