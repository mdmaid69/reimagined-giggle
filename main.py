  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities