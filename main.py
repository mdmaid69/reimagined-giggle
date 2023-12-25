  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities