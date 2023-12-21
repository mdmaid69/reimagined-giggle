  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities