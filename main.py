def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
  import os
  def get_directory_name(path):
        return os.path.dirname(path)