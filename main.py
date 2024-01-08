def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)