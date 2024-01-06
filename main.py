  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)