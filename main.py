  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets