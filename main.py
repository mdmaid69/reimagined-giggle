def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size