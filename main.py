  import os
  def get_directory_name(path):
        return os.path.dirname(path)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities