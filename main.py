def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)