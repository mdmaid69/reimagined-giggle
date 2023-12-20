def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)