  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue