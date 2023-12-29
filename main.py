def calculate_average(lst):
        return sum(lst) / len(lst)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)