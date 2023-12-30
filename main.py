  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets