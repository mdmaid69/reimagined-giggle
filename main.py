  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities