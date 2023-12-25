  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)