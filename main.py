def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)