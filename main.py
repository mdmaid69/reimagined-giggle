def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid