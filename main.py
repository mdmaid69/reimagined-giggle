  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)