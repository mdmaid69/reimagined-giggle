  def sort_list(lst):
        return sorted(lst)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)