  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time