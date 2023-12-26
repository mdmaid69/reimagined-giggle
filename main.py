  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities