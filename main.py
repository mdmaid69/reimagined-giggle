def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)