  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)