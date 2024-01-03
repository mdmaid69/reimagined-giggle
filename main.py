  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities