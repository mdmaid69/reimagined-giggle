  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
def calculate_payback_period(cash_flows):
        cumulative_cash_flow = 0
        for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        if cumulative_cash_flow >= 0:
                return i
        return None