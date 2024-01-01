import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets