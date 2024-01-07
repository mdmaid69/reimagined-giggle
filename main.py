import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)