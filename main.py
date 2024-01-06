  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)