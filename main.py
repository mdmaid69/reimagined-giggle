  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))