  import os
  def split_path(path):
        return os.path.split(path)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)