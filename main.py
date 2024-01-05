  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)