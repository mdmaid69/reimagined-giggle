  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets