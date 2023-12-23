  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities