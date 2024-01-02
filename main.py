  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets