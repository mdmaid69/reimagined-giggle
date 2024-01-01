  import os
  def split_path(path):
        return os.path.split(path)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities