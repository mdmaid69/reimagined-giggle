  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities