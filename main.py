import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)