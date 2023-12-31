  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))