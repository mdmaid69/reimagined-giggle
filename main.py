def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)