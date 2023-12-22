  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)