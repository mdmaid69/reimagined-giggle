  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities