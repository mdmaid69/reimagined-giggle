  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets