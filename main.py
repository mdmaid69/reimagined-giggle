def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)