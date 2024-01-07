  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue