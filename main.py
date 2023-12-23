  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)