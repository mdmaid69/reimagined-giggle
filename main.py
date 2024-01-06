import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue