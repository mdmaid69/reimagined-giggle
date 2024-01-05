  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets