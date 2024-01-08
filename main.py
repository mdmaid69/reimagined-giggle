  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time