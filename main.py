  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities