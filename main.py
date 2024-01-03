  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)