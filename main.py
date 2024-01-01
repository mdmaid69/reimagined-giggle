  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)