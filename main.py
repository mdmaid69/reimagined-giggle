  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)