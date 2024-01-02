import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets