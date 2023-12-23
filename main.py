import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)