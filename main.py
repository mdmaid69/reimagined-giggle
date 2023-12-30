import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)