  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities