import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities