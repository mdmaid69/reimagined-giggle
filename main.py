  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)