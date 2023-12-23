  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets