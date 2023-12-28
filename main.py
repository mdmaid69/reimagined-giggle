import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets