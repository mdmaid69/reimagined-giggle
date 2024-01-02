def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid