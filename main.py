import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)