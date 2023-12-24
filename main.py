  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time