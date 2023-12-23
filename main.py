import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)