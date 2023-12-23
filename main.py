  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue