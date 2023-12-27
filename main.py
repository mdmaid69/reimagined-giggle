def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)