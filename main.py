  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue