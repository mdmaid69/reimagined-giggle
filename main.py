  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue