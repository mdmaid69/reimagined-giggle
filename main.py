import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time