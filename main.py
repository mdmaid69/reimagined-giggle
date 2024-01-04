  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue