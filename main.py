  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time