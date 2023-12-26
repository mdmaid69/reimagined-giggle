  import os
  def delete_file(file_name):
        os.remove(file_name)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities