import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_roi(gain, cost):
        return (gain - cost) / cost