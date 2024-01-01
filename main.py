def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size