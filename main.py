  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities