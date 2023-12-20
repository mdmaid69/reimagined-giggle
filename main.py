def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size