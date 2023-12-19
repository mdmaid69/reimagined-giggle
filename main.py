  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)