  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities