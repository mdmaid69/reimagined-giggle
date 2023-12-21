import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)