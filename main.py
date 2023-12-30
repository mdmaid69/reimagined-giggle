  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)