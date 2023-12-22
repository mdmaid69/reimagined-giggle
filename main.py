  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)