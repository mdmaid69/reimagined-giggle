  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)