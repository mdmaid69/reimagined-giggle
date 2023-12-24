  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)