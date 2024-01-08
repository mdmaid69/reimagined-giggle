import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities