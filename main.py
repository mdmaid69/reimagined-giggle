  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue