  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets