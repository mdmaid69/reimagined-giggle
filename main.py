  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)