  import os
  def get_base_name(path):
        return os.path.basename(path)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)