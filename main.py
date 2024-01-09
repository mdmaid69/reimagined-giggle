  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue