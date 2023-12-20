  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets