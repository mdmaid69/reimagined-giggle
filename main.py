import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import os
  def delete_file(file_name):
        os.remove(file_name)