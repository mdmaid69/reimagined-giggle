def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)