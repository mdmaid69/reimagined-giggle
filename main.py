  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue