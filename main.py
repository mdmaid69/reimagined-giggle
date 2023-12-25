  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets