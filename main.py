  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))