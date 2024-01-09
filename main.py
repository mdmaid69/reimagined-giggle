  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)