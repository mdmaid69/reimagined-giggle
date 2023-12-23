def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)