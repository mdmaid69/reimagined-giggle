import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime