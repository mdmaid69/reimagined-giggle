import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding