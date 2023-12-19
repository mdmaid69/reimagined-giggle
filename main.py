  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets