  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)