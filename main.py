  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))