def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)