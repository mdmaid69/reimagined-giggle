import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_average(lst):
        return sum(lst) / len(lst)