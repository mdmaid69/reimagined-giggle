def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)