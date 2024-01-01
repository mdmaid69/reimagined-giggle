def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)