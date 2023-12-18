  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)