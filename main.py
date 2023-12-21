  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)