  import os
  def get_base_name(path):
        return os.path.basename(path)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))