  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)