  import os
  def delete_file(file_name):
        os.remove(file_name)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))