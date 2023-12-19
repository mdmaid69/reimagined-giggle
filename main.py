  def remove_duplicates(lst):
        return list(set(lst))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)