  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)