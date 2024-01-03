  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)