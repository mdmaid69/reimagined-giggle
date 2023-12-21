  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)