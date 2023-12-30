import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)