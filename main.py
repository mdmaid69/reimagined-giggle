  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue