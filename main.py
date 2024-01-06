def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)