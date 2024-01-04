  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))