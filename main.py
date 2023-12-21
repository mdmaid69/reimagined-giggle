  import os
  def get_directory_name(path):
        return os.path.dirname(path)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)