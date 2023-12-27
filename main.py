  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)