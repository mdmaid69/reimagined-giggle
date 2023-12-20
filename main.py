  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))