import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"