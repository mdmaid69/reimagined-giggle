  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)