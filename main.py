  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities