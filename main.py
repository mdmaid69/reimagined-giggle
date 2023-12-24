import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)