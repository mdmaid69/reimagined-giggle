  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities