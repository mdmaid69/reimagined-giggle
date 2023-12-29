import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]