  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)