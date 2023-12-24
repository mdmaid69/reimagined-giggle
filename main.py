  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets