def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns