  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities