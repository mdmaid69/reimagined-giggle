  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities