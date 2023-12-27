def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns