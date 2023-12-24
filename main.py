  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
def calculate_irr(cash_flows):
        rate = 0.1
        for _ in range(100):
        npv = sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
        if abs(npv) < 1e-6:
                return rate
        rate += 0.01
        return None