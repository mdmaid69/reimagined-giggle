  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps