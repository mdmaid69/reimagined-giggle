  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities