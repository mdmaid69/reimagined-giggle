  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)