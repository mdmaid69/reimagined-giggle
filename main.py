  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))