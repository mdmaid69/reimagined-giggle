  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities