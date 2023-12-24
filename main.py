  import os
  def get_current_directory():
        return os.getcwd()
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities