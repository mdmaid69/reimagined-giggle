  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)