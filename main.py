def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)