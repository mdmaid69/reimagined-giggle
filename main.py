def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)