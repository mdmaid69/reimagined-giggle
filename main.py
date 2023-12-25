  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities