def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime