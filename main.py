def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)