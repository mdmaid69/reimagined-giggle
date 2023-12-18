  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)