  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue