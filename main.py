  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)