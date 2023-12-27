def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime