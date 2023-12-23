def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value