  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)