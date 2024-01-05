  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)