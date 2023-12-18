def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)