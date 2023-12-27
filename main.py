  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets