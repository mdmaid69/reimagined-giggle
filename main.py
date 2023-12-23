  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)