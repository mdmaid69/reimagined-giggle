  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities