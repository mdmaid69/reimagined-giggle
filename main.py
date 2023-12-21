import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  def count_elements(lst):
        return len(lst)