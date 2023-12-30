def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  import os
  def get_base_name(path):
        return os.path.basename(path)