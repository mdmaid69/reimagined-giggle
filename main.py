  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def calculate_payback_period(cash_flows):
        cumulative_cash_flow = 0
        for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        if cumulative_cash_flow >= 0:
                return i
        return None