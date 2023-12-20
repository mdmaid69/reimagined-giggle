  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)